from django.db import models

# Create your models here.
class Equipe(models.Model):
    nome_equipe = models.CharField(verbose_name= 'Nome da Equipe' )
    