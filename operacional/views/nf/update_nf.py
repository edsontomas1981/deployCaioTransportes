from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Classes.dtc import Dtc 
from Classes.utils import dprint,dpprint,checaCamposJson
from operacional.models.dtc import Dtc as MdlDtc
from operacional.classes.nfe_caio import NotaFiscalManager
import json


@login_required(login_url='/auth/entrar/')
def update_status_nf (request):
    if request.method == 'GET':
        return JsonResponse({'status': "update"})
    elif request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            NotaFiscalManager.update_nota_fiscal_status(data.get('idNf'),data.get('numNf'))
            return JsonResponse({'status':200})
        except:
            return JsonResponse({'status':404,'message':'erro interno'}) #Cadastro efetuado com sucesso