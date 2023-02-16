from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Admin(models.Model):
    nome = models.CharField(max_length=200, null=True, verbose_name= 'Nome')
    endereço = models.CharField(max_length=200, null=True, verbose_name= 'Endereço' )
    cpf = models.IntegerField(max_length=11, null=True, verbose_name= 'CPF' )
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
