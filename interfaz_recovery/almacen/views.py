from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'form_sol_material/index.html')
    