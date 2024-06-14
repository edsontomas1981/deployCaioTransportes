from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth import get_user_model
from operacional.models.ocorrencias_notas_fiscais import OcorrenciaNotasFiscais
from operacional.models.tipo_ocorrencias import TipoOcorrencias
from operacional.models.nfe_caio import Nota_fiscal_Caio_Transportes

class OcorrenciaNotasFiscaisManager:
    @classmethod
    def get_ocorrencia_by_id(cls, ocorrencia_id):
        try:
            return OcorrenciaNotasFiscais.objects.get(id=ocorrencia_id)
        except OcorrenciaNotasFiscais.DoesNotExist:
            return None

    @classmethod
    def get_all_ocorrencias(cls):
        return OcorrenciaNotasFiscais.objects.all()

    @classmethod
    def lista_todas_ocorrencias(cls):
        ocorrencias = cls.get_all_ocorrencias()
        lista_ocorrencias = []
        for ocorrencia in ocorrencias:
            lista_ocorrencias.append(ocorrencia.to_dict())
        return lista_ocorrencias

    @staticmethod
    def save_or_update(instancia, dados):
        chaves_necessarias = [
            'ocorrencia_fk', 'nota_fiscal_fk', 'observacao', 
            'data', 'criado_por', 'atualizado_por'
        ]

        if not all(chave in dados for chave in chaves_necessarias):
            raise ValueError("Dados incompletos para salvar/atualizar ocorrência.")

        instancia.ocorrencia_fk = TipoOcorrencias.objects.get(id=dados['ocorrencia_fk'])
        instancia.nota_fiscal_fk = Nota_fiscal_Caio_Transportes.objects.get(id=dados['nota_fiscal_fk'])
        instancia.observacao = dados.get('observacao')
        instancia.data = dados.get('data')
        instancia.criado_por = get_user_model().objects.get(id=dados['criado_por'])
        instancia.atualizado_por = get_user_model().objects.get(id=dados['atualizado_por'])
        instancia.updated_at = timezone.now()

    @classmethod
    def create_ocorrencia(cls, dados):
        obj_ocorrencia = OcorrenciaNotasFiscais()
        cls.save_or_update(obj_ocorrencia, dados)
        obj_ocorrencia.created_at = timezone.now()
        obj_ocorrencia.save()
        return 200

    @classmethod
    def update_ocorrencia(cls, id_ocorrencia, dados):
        try:
            if not OcorrenciaNotasFiscais.objects.filter(id=id_ocorrencia).exists():
                raise ValueError(f"A ocorrência com o ID {id_ocorrencia} não foi encontrada.")

            obj_ocorrencia = OcorrenciaNotasFiscais.objects.get(id=id_ocorrencia)
            cls.save_or_update(obj_ocorrencia, dados)
            obj_ocorrencia.save()
            return 200
        except Exception as e:
            return str(e)

    @classmethod
    def delete_ocorrencia(cls, id_ocorrencia):
        try:
            if not OcorrenciaNotasFiscais.objects.filter(id=id_ocorrencia).exists():
                raise ValueError(f"A ocorrência com o ID {id_ocorrencia} não foi encontrada.")

            obj_ocorrencia = OcorrenciaNotasFiscais.objects.get(id=id_ocorrencia)
            obj_ocorrencia.delete()
            return 200
        except Exception as e:
            return str(e)
