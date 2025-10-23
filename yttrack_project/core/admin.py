from django.contrib import admin
from .models import Quadro
from .models import Video


@admin.register(Quadro)
class QuadroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado_em')
    search_fields = ('nome',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'quadro', 'watched', 'criado_em')
    list_filter = ('watched', 'quadro')
    search_fields = ('titulo',)
    readonly_fields = ('criado_em',)