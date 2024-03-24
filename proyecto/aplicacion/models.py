from django.db import models

class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    dni = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_completo

class Moto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    modelo = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    año_fabricacion = models.IntegerField()
    cilindrada = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.modelo
    
class Reparacion(models.Model):
    descripcion = models.TextField()
    fecha = models.DateField()
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    kilometros = models.IntegerField()

    def __str__(self):
        return f"Reparacion {self.id}"
