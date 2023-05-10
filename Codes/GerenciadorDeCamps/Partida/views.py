from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import Partidaform

from .models import Partida

# Create your views here.

def listar(request):
    Partidas = Partida.objects.all()
    context = {
        "partidas": Partidas
    }
    return render(request, 'partidas/listar.html', context)

def detail(request, partida_id):
    Partidas = Partida.objects.get(pk=partida_id)
    context = {
        "partidas": Partidas
    }
    return render(request, 'partidas/detail.html', context)


def criar(request):
    
    if request.method == "POST":
        form = Partidaform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/partidas")
    else:
        form = Partidaform()
    
    context ={
        'form': form
    }
    
    return render(request, "partidas/formCriar.html", context)


def excluir(request, partida_id):
    
    Partida.objects.get(pk=partida_id).delete()
    
    return HttpResponseRedirect("/partidas")    


def editar(request, partida_id):
    Partidas = Partida.objects.get(pk=partida_id)
    
    if request.method == "POST":
        form = Partidaform(request.POST, instance=Partidas)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/partidas")
    else:
        form = Partidaform(instance=Partidas)
    
    context ={
        'form': form,
        'partida_id': partida_id
    }
    
    return render(request, "partidas/formEditar.html", context)