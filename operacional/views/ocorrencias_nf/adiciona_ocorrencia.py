from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
from operacional.models.tipo_ocorrencias import TipoOcorrencias
from operacional.classes.ocorrencias_manager import OcorrenciaNotasFiscaisManager
from django.conf import settings
import json
import os


from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

@login_required(login_url='/auth/entrar/')
@require_http_methods(["POST","GET"])
def add_ocorrencia(request):
        try:
            data = request.POST
            id_ocorrencia = data.get('idNf')
            ocorrencia_fk = data.get('ocorrencia_fk')
            nota_fiscal_fk = data.get('nota_fiscal_fk')
            observacao = data.get('observacao')
            data_ocorrencia = data.get('data')
            criado_por = data.get('criado_por')
            atualizado_por = data.get('atualizado_por')
            
            # Salve a imagem no disco
            if 'imagem' in request.FILES:
                imagem = request.FILES['imagem']
                image_path = os.path.join('ocorrencia_imagens', imagem.name)
                path = default_storage.save(image_path, ContentFile(imagem.read()))
                imagem_path = os.path.join(settings.MEDIA_URL, path)
            else:
                imagem_path = ''

            # Atualize a ocorrência no banco de dados
            dados = {
                'ocorrencia_fk': ocorrencia_fk,
                'nota_fiscal_fk': nota_fiscal_fk,
                'observacao': observacao,
                'data': data_ocorrencia,
                'criado_por': criado_por,
                'atualizado_por': atualizado_por,
                'imagem_path': imagem_path
            }

            
            print(dados)

            status = OcorrenciaNotasFiscaisManager.create_ocorrencia(dados)
            return JsonResponse({'status': status})
        except Exception as e:
            return JsonResponse({'status': 404, 'message': 'erro interno', 'error': str(e)})
