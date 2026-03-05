from django.contrib import admin

from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "numero_documento", "telefono", "activo")
    search_fields = ("nombre", "apellido", "numero_documento")
    list_filter = ("activo",)