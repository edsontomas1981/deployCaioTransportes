from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Classes.dtc import Dtc 
from Classes.utils import dprint,dpprint,checaCamposJson
from operacional.models.dtc import Dtc as MdlDtc
from operacional.classes.nfe_caio import NotaFiscalManager
from operacional.classes.manifesto_caio_transportes import ManifestoCaioTransportesManager
import json


@login_required(login_url='/auth/entrar/')
def read_nf_chave_acesso (request):
    if request.method == 'GET':
            nota_fiscal = NotaFiscalManager.get_nota_fiscal_by_chave_acesso('4')
            ManifestoCaioTransportesManager.add_nota_manifesto(nota_fiscal,8)
            return JsonResponse({'status':200,'nota_fiscal':nota_fiscal.to_dict()}) #Cadastro efetuado com sucesso
    elif request.method == 'POST':
        try:
            # data = json.loads(request.body.decode('utf-8'))
            nota_fiscal = NotaFiscalManager.get_nota_fiscal_by_id('35240517650634000192550010000131851092837821')
            
            return JsonResponse({'status':200,'nota_fiscal':nota_fiscal.to_dict()}) #Cadastro efetuado com sucesso
        except:
            return JsonResponse({'status':404})