import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from operacional.models.nfe_caio import Nota_fiscal_Caio_Transportes
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

class NotaFiscalNaoEncontrada(Exception):
    """Exceção personalizada para indicar que a nota fiscal não foi encontrada."""

class NotaFiscalManager:
    def __init__(self):
        self.obj_nota_fiscal = None

    @classmethod
    def get_nota_fiscal_by_id(cls, nota_fiscal_id):
        try:
            return Nota_fiscal_Caio_Transportes.objects.get(id=nota_fiscal_id)
        except Nota_fiscal_Caio_Transportes.DoesNotExist:
            return None

    @classmethod
    def get_nota_fiscal_by_nota_fiscal(cls, nota_fiscal):
        try:
            return Nota_fiscal_Caio_Transportes.objects.get(num_nf=nota_fiscal)
        except Nota_fiscal_Caio_Transportes.DoesNotExist:
            return None

    @classmethod
    def get_nota_fiscal_by_chave_acesso(cls, chave_acesso):
        try:
            return Nota_fiscal_Caio_Transportes.objects.get(chave_acesso=chave_acesso)
        except Nota_fiscal_Caio_Transportes.DoesNotExist:
            return None

    @classmethod
    def get_all_notas_fiscais(cls):
        return Nota_fiscal_Caio_Transportes.objects.all()

    @classmethod
    def lista_todas_notas_fiscais(cls):
        notas_fiscais = cls.get_all_notas_fiscais()
        lista_notas_fiscais = []
        for nota in notas_fiscais:
            lista_notas_fiscais.append(nota.to_dict())
        return lista_notas_fiscais

    @staticmethod
    def save_or_update(instancia, dados):
        chaves_necessarias = [
            'chave_acesso', 'num_nf', 'natureza', 'volume', 
            'peso', 'valor_nf', 'usuario_cadastro'
        ]

        if not all(chave in dados for chave in chaves_necessarias):
            raise ValueError("Dados incompletos para salvar/atualizar nota fiscal.")

        nota_existente = Nota_fiscal_Caio_Transportes.objects.filter(chave_acesso=dados.get('chave_acesso')).first()

        if nota_existente :
            raise ValueError("Chave de acesso já cadastrada.")

        instancia.chave_acesso = dados.get('chave_acesso')
        instancia.remetente_fk = dados.get('remetente_fk')
        instancia.destinatario_fk = dados.get('destinatario_fk')
        instancia.num_nf = dados.get('num_nf')
        instancia.data_emissao = dados.get('data_emissao', "2024/01/01")
        instancia.natureza = dados.get('natureza')
        instancia.volume = dados.get('volume')
        instancia.peso = dados.get('peso')
        instancia.valor_nf = dados.get('valor_nf')
        instancia.usuario_cadastro = get_user_model().objects.get(id=dados['usuario_cadastro'])
        instancia.usuario_ultima_atualizacao = get_user_model().objects.get(id=dados['usuario_cadastro'])
        instancia.data_ultima_atualizacao = timezone.now()

    @classmethod
    def create_nota_fiscal(cls, dados):
        try:
            obj_nota_fiscal = Nota_fiscal_Caio_Transportes()
            cls.save_or_update(obj_nota_fiscal, dados)
            obj_nota_fiscal.data_cadastro = timezone.now()
            obj_nota_fiscal.save()
            return 200
        except Exception as e:
            return str(e)

    @classmethod
    def update_nota_fiscal(cls, id_nota_fiscal, dados):
        try:
            if not Nota_fiscal_Caio_Transportes.objects.filter(id=id_nota_fiscal).exists():
                raise ValueError(f"A nota fiscal com o ID {id_nota_fiscal} não foi encontrada.")

            obj_nota_fiscal = Nota_fiscal_Caio_Transportes.objects.get(id=id_nota_fiscal)
            cls.save_or_update(obj_nota_fiscal, dados)
            obj_nota_fiscal.save()
            return 200
        except Exception as e:
            return str(e)

    @classmethod
    def delete_nota_fiscal(cls, id_nota_fiscal):
        try:
            if not Nota_fiscal_Caio_Transportes.objects.filter(id=id_nota_fiscal).exists():
                raise ValueError(f"A nota fiscal com o ID {id_nota_fiscal} não foi encontrada.")

            obj_nota_fiscal = Nota_fiscal_Caio_Transportes.objects.get(id=id_nota_fiscal)
            obj_nota_fiscal.delete()
            return 200
        except Exception as e:
            return str(e)

    @classmethod
    def update_nota_fiscal_status(cls, id_nota_fiscal, new_status):
        try:
            obj_nota_fiscal = Nota_fiscal_Caio_Transportes.objects.get(id=id_nota_fiscal)
        except Nota_fiscal_Caio_Transportes.DoesNotExist:
            raise NotaFiscalNaoEncontrada(f"A nota fiscal com o ID {id_nota_fiscal} não foi encontrada.")

        obj_nota_fiscal.status = new_status
        obj_nota_fiscal.save()

        return JsonResponse({"id": obj_nota_fiscal.id, "message": "Status atualizado com sucesso"}, status=204)
