from django.db import models

class Acolchados(models.Model):
    TAMANIO_VALUES = [
        ("twin", "Twin"),
        ("queen", "Queen"),
        ("king", "King")
        ]
    tamanio=models.CharField(max_length=10,choices=TAMANIO_VALUES,verbose_name="Tamaño")
    
    color=models.CharField(max_length=20,verbose_name="Color")
    composicion=models.CharField(max_length=20,verbose_name="Composición")
    fecha_fabricacion=models.DateField(blank=True,null=True,verbose_name="Fecha de Fabricación")
    imagen_acolchado=models.ImageField(upload_to="imagenes",blank=True,null=True)
    
    
    def __str__(self):
        return f"{self.tamanio} {self.color}"


class Sabana(models.Model):
    TAMANIO_VALUES = [
        ("twin", "Twin"),
        ("queen", "Queen"),
        ("king", "King")
        ]
    tamanio=models.CharField(max_length=10,choices=TAMANIO_VALUES,verbose_name="Tamaño")
    
    color=models.CharField(max_length=20,verbose_name="Color")
    composicion=models.CharField(max_length=20,verbose_name="Composición")
    hilos=models.IntegerField(verbose_name="Hilos")
    fecha_fabricacion=models.DateField(blank=True,null=True,verbose_name="Fecha de Fabricación")
    imagen_sabana= models.ImageField(upload_to="imagenes",blank=True,null=True)
    
    def __str__(self):
        return f"{self.composicion} {self.color}"
    
class Frazada(models.Model):
    TAMANIO_VALUES = [
        ("twin", "Twin"),
        ("queen", "Queen"),
        ("king", "King")
        ]
    ESTILO_VALUES = [
        ("liso", "Liso"),
        ("rústico", "Rústico"),
        ("estampado", "Estampado")
        ]
    tamanio=models.CharField(max_length=10,choices=TAMANIO_VALUES,verbose_name="Tamaño")
    
    color=models.CharField(max_length=20,verbose_name="Color")
    estilo=models.CharField(max_length=10,choices=ESTILO_VALUES,verbose_name="Estilo")
    fecha_fabricacion=models.DateField(blank=True,null=True,verbose_name="Fecha de Fabricación")
    imagen_frazada=models.ImageField(upload_to="imagenes",blank=True,null=True)
    
    def __str__(self):
        return f"{self.color} {self.estilo}"