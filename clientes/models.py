from django.db import models
from django.core.exceptions import ValidationError
import re

class Cliente(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ("DNI", "DNI"),
        ("CUIT", "CUIT"),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO_CHOICES)
    numero_documento = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido or ''}"
    
    def clean(self):
        if not self.numero_documento:
            raise ValidationError("Debe ingresar un número de documento.")

        numero = re.sub(r"\D", "", self.numero_documento)#\D= cualquir cosa que no sea numero, reeplazala por vacio ""

        if not numero:
            raise ValidationError("El documento debe contener solo números.")

        if self.tipo_documento == "DNI":
            if len(numero) not in [7, 8]:
                raise ValidationError("El DNI debe tener 7 u 8 dígitos.")

        if self.tipo_documento == "CUIT":
            if len(numero) != 11:
                raise ValidationError("El CUIT debe tener 11 dígitos.")

        self.numero_documento = numero

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
