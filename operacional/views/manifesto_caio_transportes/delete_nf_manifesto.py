from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from operacional.classes.manifesto_caio_transportes import ManifestoCaioTransportesManager
from operacional.classes.nfe_caio import NotaFiscalManager
import json

@login_required(login_url='/auth/entrar/')
@require_http_methods(["POST"])
def delete_nota_manifesto(request):
    """
    Remove uma nota fiscal de um manifesto.

    Parâmetros:
    - request: Objeto HttpRequest com os dados do corpo da requisição em JSON.

    Retorna:
    - JsonResponse com o status da operação e os detalhes do manifesto.

    Campos esperados no corpo da requisição:
    - idNumNf: ID da nota fiscal a ser removida.
    - numManifesto: ID do manifesto do qual a nota fiscal será removida.
    """
    try:
        data = json.loads(request.body.decode('utf-8'))

        # Campos obrigatórios para remover uma nota fiscal de um manifesto
        required_fields = ['idNumNf', 'numManifesto']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return JsonResponse({'status': 'error', 'message': f'Campos obrigatórios faltando: {", ".join(missing_fields)}'}, status=400)

        nota_fiscal_id = data.get('idNumNf')
        manifesto_id = data.get('numManifesto')

        
        # Remover a nota fiscal do manifesto
        response = ManifestoCaioTransportesManager.remove_nota_manifesto(nota_fiscal_id, manifesto_id)

        if response.status_code != 200:
            return response  # Retorna a resposta de erro apropriada de remove_nota_manifesto

        manifesto = ManifestoCaioTransportesManager.get_manifesto_by_id(manifesto_id)
        if not manifesto:
            return JsonResponse({'status': 'error', 'message': 'Manifesto não encontrado.'}, status=404)

        nota = NotaFiscalManager.get_nota_fiscal_by_id(data.get('idNumNf'))
        nota.status = 1
        nota.save()
        
        return JsonResponse({'status': 'success', 'manifesto': manifesto.to_dict()}, status=200)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Erro ao decodificar JSON.'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
