from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
from operacional.classes.manifesto_caio_transportes import ManifestoCaioTransportesManager
from operacional.classes.motorista import MotoristaManager
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@require_http_methods(["POST","GET"])
def get_documentos(request):
    try:
        data = json.loads(request.body)

        motorista = MotoristaManager()
        motorista.read_motorista_by_cpf(data.get('cpf'))

        manifesto = ManifestoCaioTransportesManager.get_last_manifesto_by_motorista(motorista.obj_motorista.id)

        return ManifestoCaioTransportesManager.get_notas_by_manifesto(manifesto.id)

    except ValidationError as ve:
        return JsonResponse({'status': 400, 'error': f'Erro de validação: {str(ve)}'})
    
    except Exception as e:
        return JsonResponse({'status': 500, 'error': f'Erro desconhecido: {str(e)}'})