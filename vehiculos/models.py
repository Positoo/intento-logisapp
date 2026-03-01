from django.db import models

class Vehiculo(models.Model):

    ESTADO_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('EN_RUTA', 'En ruta'),
        ('MANTENIMIENTO', 'En mantenimiento'),
        ('FUERA_DE_SERVICIO', 'Fuerda de servicio'),
    ]

    patente = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.PositiveIntegerField()
    capacidad_carga_kg = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='DISPONIBLE'
    )

    def __str__(self):
        return f"{self.patente} - {self.marca} {self.modelo}"