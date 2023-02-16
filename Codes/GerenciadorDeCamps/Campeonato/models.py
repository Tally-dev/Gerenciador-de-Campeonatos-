from django.db import models

# Create your models here.
class Campeonato(models.Model):
    nome_camp = models.CharField(verbose_name= 'Nome do Campeonato', max_length=100)
    qtd_equipe = models.IntegerField(verbose_name= 'Quantidade de Equipes')
    tipo_partida = models.CharField(verbose_name= ' Tipo de Partida')
    