from operacional.models.manifesto_caio_transportes import ManifestoCaioTransportes
from operacional.models.nfe_caio import Nota_fiscal_Caio_Transportes
from operacional.models.motoristas import Motorista
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.utils import timezone

class ManifestoCaioTransportesManager:
    @classmethod
    def get_manifesto_by_id(cls, manifesto_id):
        try:
            return ManifestoCaioTransportes.objects.get(id=manifesto_id)
        except ManifestoCaioTransportes.DoesNotExist:
            return None

    @classmethod
    def get_all_manifestos(cls):
        return ManifestoCaioTransportes.objects.all()

    @staticmethod
    def save_or_update(instancia, dados):
        chaves_necessarias = ['motorista_fk', 'nota_fiscal_fk', 'usuario']

        if not all(chave in dados for chave in chaves_necessarias):
            raise ValueError("Dados incompletos para salvar/atualizar manifesto.")

        instancia.motorista_fk = Motorista.objects.get(id=dados['motorista_fk'])
        
        # Assuming nota_fiscal_fk is a list of IDs
        notas_fiscais = Nota_fiscal_Caio_Transportes.objects.filter(id__in=dados['nota_fiscal_fk'])
        instancia.nota_fiscal_fk.set(notas_fiscais)
        
        instancia.usuario_ultima_atualizacao = get_user_model().objects.get(id=dados['usuario'].id)
        instancia.data_ultima_atualizacao = timezone.now()

    @classmethod
    def create_manifesto(cls, dados):
        obj_manifesto = ManifestoCaioTransportes()
        cls.save_or_update(obj_manifesto, dados)
        usuario = dados.get('usuario')
        obj_manifesto.usuario_cadastro = get_user_model().objects.get(id=usuario.id)
        obj_manifesto.data_cadastro = timezone.now()
        obj_manifesto.save()
        return 200

    @classmethod
    def update_manifesto(cls, id_manifesto, dados):
        try:
            if not ManifestoCaioTransportes.objects.filter(id=id_manifesto).exists():
                raise ValueError(f"O manifesto com o ID {id_manifesto} não foi encontrado.")

            obj_manifesto = ManifestoCaioTransportes.objects.get(id=id_manifesto)
            cls.save_or_update(obj_manifesto, dados)
            obj_manifesto.save()
            return 200
        except Exception as e:
            return str(e)

    @classmethod
    def delete_manifesto(cls, id_manifesto):
        try:
            if not ManifestoCaioTransportes.objects.filter(id=id_manifesto).exists():
                raise ValueError(f"O manifesto com o ID {id_manifesto} não foi encontrado.")

            obj_manifesto = ManifestoCaioTransportes.objects.get(id=id_manifesto)
            obj_manifesto.delete()
            return 200
        except Exception as e:
            return str(e)

    @classmethod
    def buscar_todos_manifestos_por_id(cls, id):
        return ManifestoCaioTransportes.objects.filter(id=id)