from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Admin(models.Model):
    nome = models.CharField(max_length=200, null=True, verbose_name= 'Nome')
    endereço = models.CharField(max_length=200, null=True, verbose_name= 'Endereço' )
    cpf = models.IntegerField(max_length=11, null=True, verbose_name= 'CPF' )
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)


 
class Usuario (models.Model):
    nome = models.CharField(verbose_name= 'Nome', max_length= 100 )
    email = models.CharField(verbose_name= 'Emaail', max_length= 50 )
    senha = models.CharField(verbose_name= 'Senha', max_length= 20)
    cpf = models.CharField(verbose_name= 'Cpf', max_length= 14)

    def cadastrar(self):
        return  "Aqui vai cadastrar Pessoa"

        