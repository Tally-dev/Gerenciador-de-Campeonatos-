from django.db import models

class Campeonato(models.Model):
    nome = models.CharField(max_length=200, verbose_name= 'Nome', null= True )
    qtdequipe = models.IntegerField(max_length=2, verbose_name= 'Quantidade de equipes', null= True )
    tipopartida = models.CharField(max_length=200, verbose_name= 'Tipo de partida', null= True )
    
    def __str__(self):
        return self.nome
