from django.contrib import admin
from apps.plataforma.models import *
# Imagem, Cidade, DiasVisita, Horario, Imovel, Visitas


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = (
        'rua', 'valor', 'quartos', 'tamanho', 'cidade', 'tipo', 'tipo_imovel',
    )
    list_editable = (
        'valor', 'tipo',
    )
    list_filter = (
        'cidade', 'tipo', 'tipo_imovel',
    )


admin.site.register(Imagem)
admin.site.register(Cidade)
admin.site.register(DiasVisita)
admin.site.register(Horario)
# admin.site.register(Imovel)
admin.site.register(Visitas)
