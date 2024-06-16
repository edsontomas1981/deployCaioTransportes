from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils import timezone
from operacional.models.motoristas import Motorista
from operacional.models.nfe_caio import Nota_fiscal_Caio_Transportes
class ManifestoCaioTransportes (models.Model):
    # Informações específicas do emissor do CTe
    motorista_fk=models.ForeignKey(Motorista, on_delete=models.CASCADE)
    nota_fiscal_fk = models.ManyToManyField(Nota_fiscal_Caio_Transportes, on_delete=models.CASCADE)
    # Informações de usuário e data/hora
    usuario_cadastro = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='criador_emissor')
    usuario_ultima_atualizacao = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='atualizador_emissor')
    data_cadastro = models.DateTimeField(null=True)
    data_ultima_atualizacao = models.DateTimeField(default=timezone.now)  
