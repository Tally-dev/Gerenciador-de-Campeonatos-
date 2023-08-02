from django.db import models

class Campeonato(models.Model):

    TIPOS =(
        ("1", "Ponto Corrido"),
        ("2", "Mata-Mata"),
        ("3", "Fase de Grupo/Mata-Mata"))

    nome = models.CharField(max_length=200, verbose_name= 'Nome', null= True )
    qtdequipe = models.IntegerField( verbose_name= 'Quantidade de equipes', null= True )
    tipopartida = models.CharField(max_length=1,choices=TIPOS, verbose_name= 'Tipo de partida', null= True )
    
    def __str__(self):
        return self.nome
