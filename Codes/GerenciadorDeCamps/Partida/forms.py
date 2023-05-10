from django.forms import ModelForm

from .models import Partida


class Partidaform(ModelForm):
    
    class Meta:
        model = Partida
        fields = "__all__"