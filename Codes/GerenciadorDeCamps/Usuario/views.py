from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from Usuario.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def register(request):
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/accounts/login")
    else:
        form = CustomUserCreationForm()
    
    context ={
        'form': form
    }
    
    return render(request, "registration/register.html", context)

def home(request):
    return render(request, 'index.html')
