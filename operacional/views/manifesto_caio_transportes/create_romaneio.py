from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
import json
from operacional.classes.veiculo import VeiculoManager
from operacional.classes.motorista import MotoristaManager
from operacional.classes.manifesto_caio_transportes import ManifestoCaioTransportesManager

@login_required(login_url='/auth/entrar/')
@require_http_methods(["POST"])
def create_romaneio(request):
    """
    Cria um novo romaneio com base nos dados fornecidos na requisição POST.

    Requer que o usuário esteja autenticado.

    Parâmetros esperados no corpo da requisição JSON:
        - 'cpf': CPF do motorista
        - 'placa': Placa do veículo

    Retorna:
        JsonResponse com status e mensagem de sucesso ou erro.
    """
    # try:
        # Carrega os dados da requisição
    data = json.loads(request.body)

    # Campos obrigatórios para adicionar um motorista a um manifesto
    required_fields = ['cpf', 'placa']
    
    # Verifica se os campos obrigatórios estão presentes
    for field in required_fields:
        if field not in data:
            return JsonResponse({'status': 400, 'error': f'Campo {field} é obrigatório.'}, status=400)

    # Obtém o veículo com base na placa fornecida
    veiculo = VeiculoManager.get_veiculo_placa(data.get('placa'))
    if not veiculo:
        return JsonResponse({'status': 400, 'error': 'Veículo não encontrado.'}, status=400)

    # Obtém o motorista com base no CPF fornecido
    obj_motorista = MotoristaManager()
    obj_motorista.read_motorista_by_cpf(data.get('cpf'))
    motorista = obj_motorista.obj_motorista
    if not motorista:
        return JsonResponse({'status': 400, 'error': 'Motorista não encontrado.'}, status=400)

    # Obtém o usuário autenticado
    usuario = request.user

    # Prepara os dados para criar o manifesto
    dados = {
        'motorista_fk': motorista,
        'veiculo_fk': veiculo,
        'usuario': usuario
    }

    # Cria o manifesto
    status,manifesto = ManifestoCaioTransportesManager.create_manifesto(dados)

    # Retorna uma resposta JSON de sucesso
    return JsonResponse({'status': 200, 'message': 'Romaneio criado com sucesso.','manifesto':manifesto.to_dict()})

    # except json.JSONDecodeError:
    #     return JsonResponse({'status': 400, 'error': 'JSON inválido.'}, status=400)
    # except Exception as e:
    #     return JsonResponse({'status': 500, 'error': str(e)}, status=500)
