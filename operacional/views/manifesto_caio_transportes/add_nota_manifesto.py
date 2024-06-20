from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from operacional.classes.nfe_caio import NotaFiscalManager
from operacional.classes.manifesto_caio_transportes import ManifestoCaioTransportesManager
import json

from Classes.utils import string_para_data
from Classes.utils import toFloat


@login_required(login_url='/auth/entrar/')
@require_http_methods(["POST","GET"])
def add_nota_manifesto(request):
    data = json.loads(request.body)

    print(data)

    # Campos obrigatórios para adicionar um motorista a um manifesto
    required_fields = ['tipoDocumento', 'idDocumento','idRomaneio']

    nota_fiscal = get_nf(data.get('tipoDocumento'),data.get('idDocumento'))

    manifesto = ManifestoCaioTransportesManager.get_manifesto_by_id(data.get('idRomaneio'))

    resposta = ManifestoCaioTransportesManager.add_nota_manifesto(nota_fiscal,manifesto.id)

    # Retorna uma resposta JSON
    return JsonResponse({'status':'status[0]','manifesto':manifesto.to_dict()})

def get_nf(tipo_busca,termo_busca):
    if int(tipo_busca) == 1: #Busca por Chave de acesso
        return NotaFiscalManager.get_nota_fiscal_by_chave_acesso(termo_busca)
    elif int(tipo_busca) == 2: #Busca por Numero da nota fiscal: 
        return NotaFiscalManager.get_nota_fiscal_by_nota_fiscal(termo_busca)
