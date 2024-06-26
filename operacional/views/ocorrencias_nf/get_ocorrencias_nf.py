from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
from operacional.models.tipo_ocorrencias import TipoOcorrencias
from operacional.classes.ocorrencias_manager import OcorrenciaNotasFiscaisManager
import json

@login_required(login_url='/auth/entrar/')
@require_http_methods(["POST","GET"])
def get_ocorrencias_nf(request):
    try:
        data = json.loads(request.body.decode('utf-8'))

        ocorrencias = OcorrenciaNotasFiscaisManager.buscar_ocorrencias_por_nota_fiscal(data.get('idNumNf'))
        listaOcorrencia = []
        for ocorrencia in ocorrencias:
            listaOcorrencia.append(ocorrencia.to_dict())
        return JsonResponse({'status':200,'ocorrencias':listaOcorrencia})
   
    except ValidationError as ve:
        return JsonResponse({'status': 400, 'error': f'Erro de validação: {str(ve)}'})
    
    except Exception as e:
        return JsonResponse({'status': 500, 'error': f'Erro desconhecido: {str(e)}'})