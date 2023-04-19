from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from Equipe.forms import Equipeform

from .models import Equipe

# Create your views here.

def listar(request):
    Equipes = Equipe.objects.all()
    context = {
        "equipes": Equipes
    }
    return render(request, 'equipes/listar.html', context)

def detail(request, equipe_id):
    Equipes = Equipe.objects.get(pk=equipe_id)
    context = {
        "equipes": Equipes
    }
    return render(request, 'equipes/detail.html', context)


def criar(request):
    
    if request.method == "POST":
        form = Equipeform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/equipes")
    else:
        form = Equipeform()
    
    context ={
        'form': form
    }
    
    return render(request, "equipes/formCriar.html", context)


def excluir(request, equipe_id):
    
    Equipe.objects.get(pk=equipe_id).delete()
    
    return HttpResponseRedirect("/equipes")    


def editar(request, equipe_id):
    Equipes = Equipe.objects.get(pk=equipe_id)
    
    if request.method == "POST":
        form = Equipeform(request.POST, instance=Equipes)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/equipes")
    else:
        form = Equipeform(instance=Equipes)
    
    context ={
        'form': form,
        'equipe_id': equipe_id
    }
    
    return render(request, "equipes/formEditar.html", context)