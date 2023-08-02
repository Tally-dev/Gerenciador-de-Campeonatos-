from django import forms

from Equipe.models import Equipe

class Equipeform(forms.ModelForm):
    
    
    class Meta:
        model = Equipe
        fields = "__all__"