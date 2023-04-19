from django.db import models

class Equipe(models.Model):
    nome = models.CharField(max_length=200, verbose_name= 'Nome', null= True )
    participantes = models.CharField(max_length=200, verbose_name= 'Participantes', null= True )
    Campeonatos = models.CharField(max_length=200, verbose_name= 'Campeonatos', null= True )
    
    def __str__(self):
        return self.nome
