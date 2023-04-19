from django.forms import ModelForm

from Equipe.models import Equipe


class Equipeform(ModelForm):
    
    class Meta:
        model = Equipe
        fields = "__all__"