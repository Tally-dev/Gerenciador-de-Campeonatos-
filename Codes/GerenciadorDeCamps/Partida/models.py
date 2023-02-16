from django.db import models
from Campeonato.models import Campeonato

class Partida(models.Model):
    data = models.DateField(verbose_name= 'Data' )
    horario = models.TimeField(verbose_name= 'Horario' )
    local = models.CharField(verbose_name= 'Local', max_length=30)
    resultado = models.CharField(verbose_name= 'Resultado', max_length=8)
    placar = models.IntegerField(verbose_name= 'Placar')

    Campeonato = models.ForeignKey('Campeonato.Campeonato', on_delete= models.CASCADE)
    Equipe1 = models.ForeignKey('Equipe.Equipe', on_delete= models.CASCADE)
    Equipe2 = models.ForeignKey('Equipe.Equipe', on_delete= models.CASCADE)