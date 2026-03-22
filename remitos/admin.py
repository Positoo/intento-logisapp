from django.contrib import admin
from .models import Remito, HojaDeRuta, HojaDeRutaDetalle


class HojaDeRutaDetalleInline(admin.TabularInline):
    model = HojaDeRutaDetalle
    extra = 1


@admin.register(HojaDeRuta)
class HojaDeRutaAdmin(admin.ModelAdmin):
    inlines = [HojaDeRutaDetalleInline]


@admin.register(Remito)
class RemitoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fecha_creacion', 'estado')
    list_filter = ('estado',)
    search_fields = ('numero',)

admin.site.register(HojaDeRutaDetalle)
