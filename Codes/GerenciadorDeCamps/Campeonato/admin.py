from django.contrib import admin
from .models import Campeonato

class CampeonatoAdmin(admin.ModelAdmin):
    list_display = [
        "__all__"
    ]    

admin.site.register(Campeonato)