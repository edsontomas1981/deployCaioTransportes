from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import xml.etree.ElementTree as ET
from parceiros.classes.parceiros_novo import Parceiros
from enderecos.classes.endereco_novo import Enderecos
from Classes.utils import carrega_coordenadas
from operacional.classes.nfe_caio import NotaFiscalManager
from datetime import datetime


@csrf_exempt
@require_http_methods(["POST", "GET"])
def upload_xml(request):
    usuario = request.user
    if request.FILES.getlist('xml_files'):
        xml_files = request.FILES.getlist('xml_files')
        errors = []
        results = []

        for xml_file in xml_files:
            try:
                tree = ET.parse(xml_file)
                root = tree.getroot()

                # Ajuste o namespace conforme necessário
                ns = {'ns': 'http://www.portalfiscal.inf.br/nfe'}
                infNFe = root.find('.//ns:infNFe', ns)
                
                # Se infNFe não for encontrado, adicionar um erro e continuar
                if infNFe is None:
                    errors.append(f'Elemento infNFe não encontrado no arquivo {xml_file.name}')
                    continue
                
                ide = infNFe.find('ns:ide', ns)
                emit = infNFe.find('ns:emit', ns)
                dest = infNFe.find('ns:dest', ns)
                total = infNFe.find('ns:total', ns)
                transp = infNFe.find('ns:transp', ns)
                protNFe = root.find('ns:protNFe', ns)

                data = {
                    'filename': xml_file.name,
                    'ide': {
                        'cUF': get_element_text(ide, 'ns:cUF', ns),
                        'cNF': get_element_text(ide, 'ns:cNF', ns),
                        'natOp': get_element_text(ide, 'ns:natOp', ns),
                        'mod': get_element_text(ide, 'ns:mod', ns),
                        'serie': get_element_text(ide, 'ns:serie', ns),
                        'nNF': get_element_text(ide, 'ns:nNF', ns),
                        'dhEmi': get_element_text(ide, 'ns:dhEmi', ns),
                        'dhSaiEnt': get_element_text(ide, 'ns:dhSaiEnt', ns),
                        'tpNF': get_element_text(ide, 'ns:tpNF', ns),
                        'idDest': get_element_text(ide, 'ns:idDest', ns),
                        'cMunFG': get_element_text(ide, 'ns:cMunFG', ns),
                        'tpImp': get_element_text(ide, 'ns:tpImp', ns),
                        'tpEmis': get_element_text(ide, 'ns:tpEmis', ns),
                        'cDV': get_element_text(ide, 'ns:cDV', ns),
                        'tpAmb': get_element_text(ide, 'ns:tpAmb', ns),
                        'finNFe': get_element_text(ide, 'ns:finNFe', ns),
                        'indFinal': get_element_text(ide, 'ns:indFinal', ns),
                        'indPres': get_element_text(ide, 'ns:indPres', ns),
                        'procEmi': get_element_text(ide, 'ns:procEmi', ns),
                        'verProc': get_element_text(ide, 'ns:verProc', ns),
                        'volume': get_element_text(ide, 'ns:volume', ns),
                        'peso': get_element_text(ide, 'ns:peso', ns),
                        'valorNF': get_element_text(total.find('ns:ICMSTot', ns), 'ns:vNF', ns),
                        'volume': get_element_text(transp.find('ns:vol', ns), 'ns:qVol', ns),
                        'peso': get_element_text(transp.find('ns:vol', ns), 'ns:pesoB', ns),
                        'valorNF': get_element_text(total.find('ns:ICMSTot', ns), 'ns:vNF', ns),
                    },
                    'emit': {
                        'CNPJ': get_element_text(emit, 'ns:CNPJ', ns),
                        'xNome': get_element_text(emit, 'ns:xNome', ns),
                        'xFant': get_element_text(emit, 'ns:xFant', ns),
                        'xLgr': get_element_text(emit, 'ns:enderEmit/ns:xLgr', ns),
                        'nro': get_element_text(emit, 'ns:enderEmit/ns:nro', ns),
                        'xBairro': get_element_text(emit, 'ns:enderEmit/ns:xBairro', ns),
                        'cMun': get_element_text(emit, 'ns:enderEmit/ns:cMun', ns),
                        'xMun': get_element_text(emit, 'ns:enderEmit/ns:xMun', ns),
                        'UF': get_element_text(emit, 'ns:enderEmit/ns:UF', ns),
                        'CEP': get_element_text(emit, 'ns:enderEmit/ns:CEP', ns),
                        'cPais': get_element_text(emit, 'ns:enderEmit/ns:cPais', ns),
                        'xPais': get_element_text(emit, 'ns:enderEmit/ns:xPais', ns),
                        'fone': get_element_text(emit, 'ns:enderEmit/ns:fone', ns),
                        'IE': get_element_text(emit, 'ns:IE', ns),
                        'CRT': get_element_text(emit, 'ns:CRT', ns)
                    },
                    'dest': {
                        'CNPJ': get_element_text(dest, 'ns:CNPJ', ns),
                        'xNome': get_element_text(dest, 'ns:xNome', ns),
                        'xLgr': get_element_text(dest, 'ns:enderDest/ns:xLgr', ns),
                        'nro': get_element_text(dest, 'ns:enderDest/ns:nro', ns),
                        'xBairro': get_element_text(dest, 'ns:enderDest/ns:xBairro', ns),
                        'cMun': get_element_text(dest, 'ns:enderDest/ns:cMun', ns),
                        'xMun': get_element_text(dest, 'ns:enderDest/ns:xMun', ns),
                        'UF': get_element_text(dest, 'ns:enderDest/ns:UF', ns),
                        'CEP': get_element_text(dest, 'ns:enderDest/ns:CEP', ns),
                        'cPais': get_element_text(dest, 'ns:enderDest/ns:cPais', ns),
                        'xPais': get_element_text(dest, 'ns:enderDest/ns:xPais', ns),
                        'fone': get_element_text(dest, 'ns:enderDest/ns:fone', ns),
                        'indIEDest': get_element_text(dest, 'ns:indIEDest', ns),
                        'IE': get_element_text(dest, 'ns:IE', ns)
                    },
                    'infProt': {
                        'tpAmb': get_element_text(protNFe, 'ns:infProt/ns:tpAmb', ns),
                        'verAplic': get_element_text(protNFe, 'ns:infProt/ns:verAplic', ns),
                        'chNFe': get_element_text(protNFe, 'ns:infProt/ns:chNFe', ns),
                        'dhRecbto': get_element_text(protNFe, 'ns:infProt/ns:dhRecbto', ns),
                        'nProt': get_element_text(protNFe, 'ns:infProt/ns:nProt', ns),
                        'digVal': get_element_text(protNFe, 'ns:infProt/ns:digVal', ns),
                        'cStat': get_element_text(protNFe, 'ns:infProt/ns:cStat', ns),
                        'xMotivo': get_element_text(protNFe, 'ns:infProt/ns:xMotivo', ns)
                    }
                }

                # Data original
                data_original = "2024-06-05T10:51:14-03:00"

                # Remover o fuso horário
                data_sem_fuso = data_original.split("T")[0]

                # Converter para um objeto datetime
                data_objeto = datetime.strptime(data_sem_fuso, "%Y-%m-%d")

                # Formatar para YYYY-MM-DD
                data_formatada = data_objeto.strftime('%Y-%m-%d')

                remetente = checa_parceiro_cadastrado(data.get("emit"))
                destinatario = checa_parceiro_cadastrado(data.get("dest"))

                dados_nota_fiscal = {
                    'chave_acesso':data.get("infProt").get('chNFe'," "),
                    'num_nf':data.get("ide").get('dhEmi'),
                    'data_emissao':data_formatada,
                    'natureza':data.get("ide").get('natOp'),
                    'volume':data.get("ide").get('volume'),
                    'peso':data.get("ide").get('peso'),
                    'valor_nf':data.get("ide").get('valorNF'),
                    'usuario_cadastro':usuario.id,
                    'remetente_fk':remetente,
                    'destinatario_fk':destinatario,
                }
                
                NotaFiscalManager.create_nota_fiscal(dados_nota_fiscal)

                results.append(data)

            except ET.ParseError:
                errors.append(f'Erro ao parsear o arquivo {xml_file.name}')
            except AttributeError:
                errors.append(f'Elementos de CNPJ não encontrados no arquivo {xml_file.name}')

        if errors:
            return JsonResponse({'errors': errors}, status=400)

        return JsonResponse({'message': 'Arquivos XML recebidos com sucesso.', 'data': results})

    return JsonResponse({'error': 'Nenhum arquivo XML encontrado.'}, status=400)


def checa_parceiro_cadastrado(dados_parceiro):
    dados_normalizados_para_cadastro = normaliza_dados_parceiro(dados_parceiro)
    endereco = normaliza_dados_endereco(dados_parceiro)
    if not Parceiros.readParceiro(dados_parceiro.get('CNPJ')):
        endereco = cadastra_endereco(endereco)
        dados_normalizados_para_cadastro['endereco_fk'] = endereco
        return cadastra_parceiro(dados_normalizados_para_cadastro)
    else:
        return Parceiros.readParceiro(dados_parceiro.get('CNPJ'))


def cadastra_parceiro(dados_parceiro):
    return Parceiros.createParceiro(dados_parceiro)
    

def cadastra_endereco(dados_parceiro):
    return Enderecos.createEndereco(dados_parceiro)
    

def normaliza_dados_parceiro(dados_parceiro):
    return{'cnpj':dados_parceiro.get('CNPJ'),
           'razao':dados_parceiro.get('xNome'),
           'fantasia':dados_parceiro.get('xFant'," "),
           'inscr':dados_parceiro.get('IE','ISENTO'),
           }

def normaliza_dados_endereco(dados_parceiro):
    stringEndereco = dados_parceiro.get('xLgr') + ' ' + dados_parceiro.get('xBairro') + " " + dados_parceiro.get('UF')
    coords = carrega_coordenadas(stringEndereco)
    lat = None
    lng = None
    if coords:
        lat = coords[0]
        lng = coords[1]

    return{'cep':dados_parceiro.get('CEP'),
            'logradouro':dados_parceiro.get('xLgr'),
            'numero':dados_parceiro.get('nro'),
            'complemento':dados_parceiro.get('xLgr'),
            'bairro':dados_parceiro.get('xBairro'),
            'cidade':dados_parceiro.get('xMun'),
            'estado':dados_parceiro.get('UF'),
            'lat':lat,
            'lng':lng,
            }

def get_element_text(parent_element, xpath, namespaces):
    element = parent_element.find(xpath, namespaces)
    if element is not None:
        return element.text
    else:
        return None
