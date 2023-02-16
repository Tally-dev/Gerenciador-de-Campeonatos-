from django.db import models

 
class Usuario (models.Model):
    nome = models.CharField(verbose_name= 'Nome', max_length= 100 )
    email = models.CharField(verbose_name= 'Emaail', max_length= 50 )
    senha = models.CharField(verbose_name= 'Senha', max_length= 20)
    cpf = models.CharField(verbose_name= 'Cpf', max_length= 14)

    def cadastrar(self):
        return  "Aqui vai cadastrar Pessoa"