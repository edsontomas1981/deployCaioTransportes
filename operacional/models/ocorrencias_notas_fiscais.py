from django.db import models
from operacional.models.tipo_ocorrencias import TipoOcorrencias
from operacional.models.nfe_caio import Nota_fiscal_Caio_Transportes
from django.conf import settings
from django.utils import timezone

class OcorrenciaNotasFiscais(models.Model):
    ocorrencia_fk = models.ForeignKey(TipoOcorrencias, on_delete=models.CASCADE, related_name='tipo_ocorrencia', null=True)
    nota_fiscal_fk = models.ForeignKey(Nota_fiscal_Caio_Transportes, on_delete=models.CASCADE, related_name='nf_ocorrencia', null=True)
    observacao = models.CharField(max_length=70)
    data = models.DateField(null=True)
    imagem_path = models.CharField(max_length=255, blank=True, null=True)  # Alterado para armazenar o caminho da imagem
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='ocorrencia_criado_por', null=True)
    atualizado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='ocorrencia_atualizado_por', null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

