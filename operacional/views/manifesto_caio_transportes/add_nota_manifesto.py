from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
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

    # Campos obrigatórios para adicionar um motorista a um manifesto
    required_fields = ['cpfMotorista', 'idManifesto']

    
    # Retorna uma resposta JSON
    return JsonResponse({'status':200,'motoristas':'motoristas'})