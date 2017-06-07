from django.db import models

# Create your models here.

class Formulario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    comentario = models.TextField()
    def __str__(self):
            return '{}'.format(self.nombre+' '+self.apellido+' '+str(self.edad)+' '+self.email)


