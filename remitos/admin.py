from django.contrib import admin
from .models import Remito, HojaDeRuta, HojaDeRutaDetalle


class HojaDeRutaDetalleInline(admin.TabularInline):
    model = HojaDeRutaDetalle
    extra = 1


@admin.register(HojaDeRuta)
class HojaDeRutaAdmin(admin.ModelAdmin):
    inlines = [HojaDeRutaDetalleInline]


admin.site.register(Remito)
admin.site.register(HojaDeRutaDetalle)
