from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
import json
from operacional.classes.veiculo import VeiculoManager
from operacional.classes.motorista import MotoristaManager
from operacional.classes.manifesto_caio_transportes import ManifestoCaioTransportesManager

@login_required(login_url='/auth/entrar/')
@require_http_methods(["POST",'GET'])
def get_romaneio(request):
    try:
        data = json.loads(request.body)
        manifesto = ManifestoCaioTransportesManager.get_manifesto_by_id(data.get('idRomaneio')) 
        return JsonResponse({'status':200,'manifesto':manifesto.to_dict()},status=200)
    except:
        return JsonResponse({'msg':'manifesto não localizado','status':404})
    

