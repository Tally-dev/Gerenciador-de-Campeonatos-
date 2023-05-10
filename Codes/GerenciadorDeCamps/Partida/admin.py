from django.contrib import admin
from .models import Partida

class PartidaAdmin(admin.ModelAdmin):
    list_display = [
        "__all__"
    ]    

admin.site.register(Partida)