from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
from operacional.models.tipo_ocorrencias import TipoOcorrencias
import json

@login_required(login_url='/auth/entrar/')
@require_http_methods(["POST","GET"])
def update_ocorrencia(request):
    try:
        return JsonResponse({'status':'update_ocorrencia'})
    
    except ValidationError as ve:
        return JsonResponse({'status': 400, 'error': f'Erro de validação: {str(ve)}'})
    
    except Exception as e:
        return JsonResponse({'status': 500, 'error': f'Erro desconhecido: {str(e)}'})