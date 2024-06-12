from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from Classes.utils import carrega_coordenadas
from operacional.classes.nfe_caio import NotaFiscalManager
from datetime import datetime

@csrf_exempt
@login_required(login_url='/auth/entrar/')
@require_http_methods(["POST","GET"])
def read_nfs_by_dtc (request):
    try:
        notas_fiscais = NotaFiscalManager.lista_todas_notas_fiscais()
        return JsonResponse({'status':200,'nfs':notas_fiscais})
    except:
        return JsonResponse({'status':400,'nfs':{},'message':'Erro Interno'})
