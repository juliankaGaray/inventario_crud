from django.db import models

# Create your models here.
class Equipo(models.Model):
    numero_placa = models.CharField(max_length=50, unique=True)
    tipo_equipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=100)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(auto_now_add=True) 
    nota = models.TextField(null=True, blank=True)  # Campo opcional para notas
    disco_duro = models.CharField(max_length=100, null=True, blank=True)  # Campo opcional para la capacidad del disco duro
    sistema_operativo = models.CharField(max_length=50, null=True, blank=True) 
    
    def __str__(self):
        return f"{self.tipo_equipo} - {self.numero_placa}"

class Periferico(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.CharField(max_length=50)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="perifericos")
    
    def __str__(self):
        return self.nombre

class HistorialMantenimiento(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="mantenimientos")
    motivo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Mantenimiento de {self.equipo.numero_placa} el {self.fecha}" 
