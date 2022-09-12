from django.db import models

# Create your models here.
class Familiar(models.Model):
    
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    correo = models.EmailField()
    fechanacimiento = models.DateField()

