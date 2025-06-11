from django.contrib import admin
from .models import (
    InstanciaEventoCiclo, CicloAcademico, Evento, MiembroPsicopedagogia, ImagenGeneralNosotros,
    FotoEvento, ArchivoInscritos, CategoriaDeporte, EquipoCopaTecsup
)

admin.site.register(CicloAcademico)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'es_destacado', 'link_formulario')

admin.site.register(MiembroPsicopedagogia)
admin.site.register(ImagenGeneralNosotros)
admin.site.register(FotoEvento)
admin.site.register(ArchivoInscritos)
admin.site.register(CategoriaDeporte)
admin.site.register(EquipoCopaTecsup)

admin.site.register(InstanciaEventoCiclo)
