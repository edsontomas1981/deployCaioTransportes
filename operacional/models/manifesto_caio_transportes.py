from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils import timezone
from operacional.models.motoristas import Motorista
from operacional.models.nfe_caio import Nota_fiscal_Caio_Transportes
from operacional.models.veiculos import Veiculo

class ManifestoCaioTransportes (models.Model):
    # Informações específicas do emissor do CTe
    motorista_fk=models.ForeignKey(Motorista, on_delete=models.CASCADE)
    veiculo_fk=models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    nota_fiscal_fk = models.ManyToManyField(Nota_fiscal_Caio_Transportes)
    # Informações de usuário e data/hora
    usuario_cadastro = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='criador_romaneio')
    usuario_ultima_atualizacao = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='atualizador_romaneio')
    data_cadastro = models.DateTimeField(null=True)
    data_ultima_atualizacao = models.DateTimeField(default=timezone.now)  

    def to_dict(self):
        return {
            'id': self.id,
            'motorista_fk': self.motorista_fk.to_dict(),
            'veiculo_fk': self.veiculo_fk.to_dict(),
            # 'nota_fiscal_fk': [
            #     {
            #         'id': nota_fiscal.id,
            #         'numero': nota_fiscal.numero  # Assumindo que Nota_fiscal_Caio_Transportes tem um campo 'numero'
            #     } for nota_fiscal in self.nota_fiscal_fk.all()
            # ],
            # 'usuario_cadastro': {
            #     'id': self.usuario_cadastro.id,
            #     'username': self.usuario_cadastro.username  # Assumindo que User tem um campo 'username'
            # } if self.usuario_cadastro else None,
            # 'usuario_ultima_atualizacao': {
            #     'id': self.usuario_ultima_atualizacao.id,
            #     'username': self.usuario_ultima_atualizacao.username  # Assumindo que User tem um campo 'username'
            # } if self.usuario_ultima_atualizacao else None,
            # 'data_cadastro': self.data_cadastro.isoformat() if self.data_cadastro else None,
            # 'data_ultima_atualizacao': self.data_ultima_atualizacao.isoformat() if self.data_ultima_atualizacao else None,
        }