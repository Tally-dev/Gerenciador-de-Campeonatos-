from django.db import models
from Campeonato.models import Campeonato

class Partida(models.Model):
    nome = models.CharField(verbose_name='Nome da Partida', max_length= 100, null= True)
    data = models.DateField(verbose_name= 'Data', null=True, blank=True)
    horario = models.TimeField(verbose_name= 'Horario', null=True, blank=True )
    local = models.CharField(verbose_name= 'Local', max_length=30)
    resultado = models.CharField(verbose_name= 'Resultado', max_length=25,null= True)
    placar = models.IntegerField(verbose_name= 'Placar')

    Campeonato = models.ForeignKey('Campeonato.Campeonato', on_delete= models.CASCADE)
    Equipe1 = models.ForeignKey('Equipe.Equipe', on_delete= models.CASCADE, related_name="PrimeiraEquipe")
    Equipe2 = models.ForeignKey('Equipe.Equipe', on_delete= models.CASCADE, related_name="SegundaEquipe")