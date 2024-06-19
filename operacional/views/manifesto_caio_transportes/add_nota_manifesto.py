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
    """
    View para adicionar um motorista a um manifesto.
    
    Requer autenticação do usuário.
    Aceita tanto requisições POST.
    """

    # ManifestoCaioTransportesManager.add_nota_manifesto(nota_fiscal,8)


    # Campos obrigatórios para adicionar um motorista a um manifesto
    required_fields = ['cpfMotorista', 'idManifesto']

    nota_fiscal = get_nf(2,'244598')

    manifesto = ManifestoCaioTransportesManager.get_manifesto_by_id()

    # Retorna uma resposta JSON
    return JsonResponse({'status':200,'nf':nota_fiscal.to_dict()})


def get_nf(tipo_busca,termo_busca):
    if int(tipo_busca) == 1: #Busca por Chave de acesso
        return NotaFiscalManager.get_nota_fiscal_by_chave_acesso(termo_busca)
    elif int(tipo_busca) == 2: #Busca por Numero da nota fiscal: 
        return NotaFiscalManager.get_nota_fiscal_by_nota_fiscal(termo_busca)
