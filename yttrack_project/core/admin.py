from django.contrib import admin
from .models import Quadro

@admin.register(Quadro)
class QuadroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado_em')
    search_fields = ('nome',)

