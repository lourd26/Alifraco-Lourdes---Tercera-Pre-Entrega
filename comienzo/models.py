from django.db import models

class Acolchados(models.Model):
    tamanio=models.CharField(max_length=20)
    color=models.CharField(max_length=20)
    composicion=models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.tamanio} {self.color}"