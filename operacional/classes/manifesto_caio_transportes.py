from operacional.models.manifesto_caio_transportes import ManifestoCaioTransportes
from operacional.models.nfe_caio import Nota_fiscal_Caio_Transportes
from operacional.classes.nfe_caio import NotaFiscalManager
from operacional.models.motoristas import Motorista
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.http import JsonResponse

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
        chaves_necessarias = ['motorista_fk','veiculo_fk']

        if not all(chave in dados for chave in chaves_necessarias):
            raise ValueError("Dados incompletos para salvar/atualizar manifesto.")

        instancia.motorista_fk = dados.get('motorista_fk')
        instancia.veiculo_fk = dados.get('veiculo_fk')


    @classmethod
    def create_manifesto(cls, dados):
        obj_manifesto = ManifestoCaioTransportes()
        cls.save_or_update(obj_manifesto, dados)
        usuario = dados.get('usuario')
        obj_manifesto.usuario_cadastro = get_user_model().objects.get(id=usuario.id)
        obj_manifesto.data_cadastro = timezone.now()
        obj_manifesto.save()
        return 200,obj_manifesto

    @classmethod
    def add_nota_manifesto(cls, nota_fiscal, manifesto_id):
        # Obter o manifesto existente pelo ID
        obj_manifesto = ManifestoCaioTransportes.objects.get(id=manifesto_id)

        # Adicionar a nota fiscal à relação many-to-many
        obj_manifesto.nota_fiscal_fk.add(nota_fiscal)

        # Atualizar a data da última atualização
        obj_manifesto.save()

        nota_fiscal.status = 2
        nota_fiscal.save()


        return 200, obj_manifesto
    
    @classmethod
    def remove_nota_manifesto(cls, nota_fiscal_id, manifesto_id):
        try:
            # Obter o manifesto existente pelo ID
            obj_manifesto = ManifestoCaioTransportes.objects.get(id=manifesto_id)

            # Obter a nota fiscal existente pelo ID
            nota_fiscal = Nota_fiscal_Caio_Transportes.objects.get(id=nota_fiscal_id)

            # Remover a nota fiscal da relação many-to-many
            obj_manifesto.nota_fiscal_fk.remove(nota_fiscal)

            # Atualizar o status da nota fiscal
            nota_fiscal.status = 1  # ou outro status apropriado
            nota_fiscal.save()

            # Atualizar a data da última atualização do manifesto
            obj_manifesto.save()

            return JsonResponse({"status": "success", "message": "Nota fiscal removida com sucesso do manifesto."}, status=200)
        except ManifestoCaioTransportes.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Manifesto não encontrado."}, status=404)
        except Nota_fiscal_Caio_Transportes.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Nota fiscal não encontrada."}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

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
    
    @classmethod
    def get_last_manifesto_by_motorista(cls, motorista_id):
        motorista = get_object_or_404(Motorista, id=motorista_id)
        try:
            return ManifestoCaioTransportes.objects.filter(motorista_fk=motorista).order_by('-id').first()
        except ManifestoCaioTransportes.DoesNotExist:
            return None
        
    @classmethod
    def get_notas_by_manifesto(cls, manifesto_id):
        try:
            manifesto = get_object_or_404(ManifestoCaioTransportes, id=manifesto_id)
            notas = manifesto.nota_fiscal_fk.all()
            notas_dict = [nota.to_dict_app_destinatario() for nota in notas]
            return JsonResponse({"dados": notas_dict}, status=200)
        except ManifestoCaioTransportes.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Manifesto não encontrado"}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
        
    @classmethod
    def get_notas_by_manifesto_dict(cls, manifesto_id):
        try:
            manifesto = get_object_or_404(ManifestoCaioTransportes, id=manifesto_id)
            notas = manifesto.nota_fiscal_fk.all()
            notas_dict = [nota.to_dict_app_destinatario() for nota in notas]
            return  notas_dict
        except ManifestoCaioTransportes.DoesNotExist:
            return 404
        except Exception as e:
            return 500
        