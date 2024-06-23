from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from operacional.classes.nfe_caio import NotaFiscalManager
from operacional.classes.manifesto_caio_transportes import ManifestoCaioTransportesManager
import json

from Classes.utils import string_para_data
from Classes.utils import toFloat


@login_required(login_url='/auth/entrar/')
@require_http_methods(["POST", "GET"])
def add_nota_manifesto(request):
    """
    Adiciona uma nota fiscal a um manifesto.

    Parâmetros:
    - request: Objeto HttpRequest com os dados do corpo da requisição em JSON.

    Retorna:
    - JsonResponse com o status da operação e os detalhes do manifesto.

    Campos esperados no corpo da requisição:
    - tipoDocumento: Tipo de documento para busca da nota fiscal.
    - idDocumento: ID ou chave de acesso do documento.
    - idRomaneio: ID do manifesto ao qual a nota fiscal será adicionada.
    """
    try:
        data = json.loads(request.body)

        # Campos obrigatórios para adicionar uma nota fiscal a um manifesto
        required_fields = ['tipoDocumento', 'idDocumento', 'idRomaneio']
        for field in required_fields:
            if field not in data:
                return JsonResponse({'status': 'error', 'message': f'Campo {field} é obrigatório.'}, status=400)

        nota_fiscal = get_nf(data.get('tipoDocumento'), data.get('idDocumento'))
        if not nota_fiscal:
            return JsonResponse({'status': 'error', 'message': 'Nota fiscal não encontrada.'}, status=404)

        manifesto = ManifestoCaioTransportesManager.get_manifesto_by_id(data.get('idRomaneio'))
        if not manifesto:
            return JsonResponse({'status': 'error', 'message': 'Manifesto não encontrado.'}, status=404)

        status, obj_manifesto = ManifestoCaioTransportesManager.add_nota_manifesto(nota_fiscal, manifesto.id)

        if status != 200:
            return JsonResponse({'status': 'error', 'message': 'Erro ao adicionar nota fiscal ao manifesto.'}, status=500)

        return JsonResponse({'status': 'success', 'manifesto': obj_manifesto.to_dict()})
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Erro ao decodificar JSON.'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


def get_nf(tipo_busca, termo_busca):
    """
    Obtém uma nota fiscal com base no tipo e termo de busca.

    Parâmetros:
    - tipo_busca: Tipo de busca (1 para chave de acesso, 2 para número da nota fiscal).
    - termo_busca: Termo de busca (chave de acesso ou número da nota fiscal).

    Retorna:
    - Nota fiscal correspondente ao tipo e termo de busca, ou None se não for encontrada.
    """
    try:
        tipo_busca = int(tipo_busca)
        if tipo_busca == 1:  # Busca por Chave de acesso
            return NotaFiscalManager.get_nota_fiscal_by_chave_acesso(termo_busca)
        elif tipo_busca == 2:  # Busca por Número da nota fiscal
            return NotaFiscalManager.get_nota_fiscal_by_nota_fiscal(termo_busca)
        else:
            return None
    except (ValueError, NotaFiscalManager.DoesNotExist):
        return None
