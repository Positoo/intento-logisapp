from django.db import models

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
