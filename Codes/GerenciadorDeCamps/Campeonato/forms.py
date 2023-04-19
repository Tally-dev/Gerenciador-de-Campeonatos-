from django.forms import ModelForm

from .models import Campeonato


class Campeonatoform(ModelForm):
    
    class Meta:
        model = Campeonato
        fields = "__all__"