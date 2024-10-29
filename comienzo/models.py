from django.db import models

class Acolchados(models.Model):
    TAMANIO_VALUES = [
        ("twin", "Twin"),
        ("queen", "Queen"),
        ("king", "King")
        ]
    tamanio=models.CharField(max_length=10,choices=TAMANIO_VALUES,verbose_name="tamaño")
    
    color=models.CharField(max_length=20)
    composicion=models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.tamanio} {self.color}"