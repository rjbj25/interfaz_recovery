from django.shortcuts import render
from django.http import HttpResponse
from .models import Recurso, Tecnico
import logging

def index(request):
    return HttpResponse("Hello, world. You're at the almacen index.")
    
def sol_material(request):
    tecnicos = Tecnico.objects.all()
    materiales = Recurso.objects.all()
    return render(request, 'almacen/sol_material.html', {
            'tecnicos': tecnicos, 
            'materiales': materiales
        })

def form_sol_mat_sended(request):
    print(request.POST[''])
    return HttpResponse("Formulario enviado")