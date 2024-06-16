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

    def to_dict(self):
        """Converte a instância do modelo para um dicionário Python."""

        return {
            'id': self.id,
            'ocorrencia': self.ocorrencia_fk.to_dict() if self.ocorrencia_fk else None,
            'nota_fiscal': self.nota_fiscal_fk.to_dict() if self.nota_fiscal_fk else None,
            'observacao': self.observacao,
            'data': self.data.strftime('%Y-%m-%d') if self.data else None,
            'imagem_path': self.imagem_path,
            'criado_por': self.criado_por.username if self.criado_por else None,
            'atualizado_por': self.atualizado_por.username if self.atualizado_por else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }