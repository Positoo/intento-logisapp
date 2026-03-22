from django.db import models
from clientes.models import Cliente
from vehiculos.models import Vehiculo

class Remito (models.Model):

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_ruta', 'En ruta'),
        ('entregado', 'Entregado'),
    ]
    
    numero = models.CharField(max_length=20, unique=True, editable=False)
    estado = models.CharField(
        max_length=20,
        choices= ESTADO_CHOICES,
        default= 'pendiente'
    )

    # remitente (persona que trae el paquete)
    remitente_nombre = models.CharField(max_length=150)
    remitente_telefono = models.CharField(max_length=30, blank=True)
    remitente_direccion = models.CharField(max_length=200)
    
    #el cliente que puede o no estar registrado en la DB
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    #consignatario
    consignatario_nombre = models.CharField(max_length=150)

    destino = models.CharField(max_length=150)

    valor_declarado = models.DecimalField(max_digits=12, decimal_places=2)

    cantidad_bultos = models.PositiveBigIntegerField()

    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.numero
    
    #Generar el numero automaticamente

    def save(self, *args, **kwargs):

        if not self.numero:

            ultimo_remito = Remito.objects.order_by('id').last()

            if ultimo_remito:
                 ultimo_numero = int(ultimo_remito.numero[1:])
                 nuevo_numero = ultimo_numero + 1
            else:
                nuevo_numero = 1

            self.numero = f"R{nuevo_numero:08d}"

        super().save(*args, **kwargs)


#Hoja de Ruta 

class HojaDeRuta (models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.PROTECT)
    chofer = models.CharField(max_length=150)
    fecha = models.DateField()

    def __str__(self):

        return f"Hoja de Ruta {self.id} - {self.fecha}"

#Hoja de ruta Detalle

class HojaDeRutaDetalle(models.Model):

    hoja_ruta = models.ForeignKey(
        HojaDeRuta,
        on_delete=models.CASCADE,
        related_name="detalles"
    )

    remito = models.OneToOneField(
        Remito,
        on_delete=models.PROTECT
    )

    orden = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.hoja_ruta} - {self.remito}"

