from django.shortcuts import render
from django.http import HttpResponse
from .models import Carrera

def home(request):
    #return HttpResponse("<h1>Inicio</h1>")
    carreras= Carrera.objects.all()
    data={
        'carreras':carreras
        }

    return render(request,'core/home.html',data)
    

def carreras(request):
    carreras= Carrera.objects.all()
    data={
        'carreras':carreras
        }


    return render(request,'core/carreras.html',data)

def docentes(request):
    #return HttpResponse("<h1>docentes</h1>")
    return render(request,'core/docentes.html')
