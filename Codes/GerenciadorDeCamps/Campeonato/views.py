from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import Campeonatoform

from .models import Campeonato

# Create your views here.

def listar(request):
    Campeonatos = Campeonato.objects.all()
    context = {
        "campeonatos": Campeonatos
    }
    return render(request, 'campeonatos/listar.html', context)

def detail(request, campeonato_id):
    Campeonatos = Campeonato.objects.get(pk=campeonato_id)
    context = {
        "campeonatos": Campeonatos
    }
    return render(request, 'campeonatos/detail.html', context)


def criar(request):
    
    if request.method == "POST":
        form = Campeonatoform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/campeonatos")
    else:
        form = Campeonatoform()
    
    context ={
        'form': form
    }
    
    return render(request, "campeonatos/formCriar.html", context)


def excluir(request, campeonato_id):
    
    Campeonato.objects.get(pk=campeonato_id).delete()
    
    return HttpResponseRedirect("/campeonatos")    


def editar(request, campeonato_id):
    Campeonatos = Campeonato.objects.get(pk=campeonato_id)
    
    if request.method == "POST":
        form = Campeonatoform(request.POST, instance=Campeonatos)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/campeonatos")
    else:
        form = Campeonatoform(instance=Campeonatos)
    
    context ={
        'form': form,
        'campeonato_id': campeonato_id
    }
    
    return render(request, "campeonatos/formEditar.html", context)