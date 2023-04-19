from django.contrib import admin
from .models import Equipe

class EquipeAdmin(admin.ModelAdmin):
    list_display = [
        "__all__"
    ]    

admin.site.register(Equipe)