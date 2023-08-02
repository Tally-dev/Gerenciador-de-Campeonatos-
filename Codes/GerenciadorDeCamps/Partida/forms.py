from django import forms
from django.forms import TimeInput, ModelForm
from Partida.models import Partida

class Partidaform(ModelForm):
    data = forms.DateField(
        label='Data',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    horario = forms.TimeField(
        label='Horário',
        widget=forms.TimeInput(attrs={'type': 'time'})
    )

    class Meta:
        model = Partida
        fields = "__all__"
    