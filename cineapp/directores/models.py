from django.db import models


class Genero(models.Model):
    nombre=models.CharField(max_length=35,help_text=" Género de la película")

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    peliculas = models.CharField(max_length=40)
    director = models.ForeignKey('Directore',on_delete=models.SET_NULL,null=True)
    descripcion= models.TextField(max_length=100, help_text='Descripción de la pelicula')
    genero = models.ManyToManyField(Genero)
    

    def __str__(self):
        return self.peliculas



class Directore(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    fecha_Nacimiento =  models.DateField(null=True,blank=True)
    fecha_Muerte = models.DateField('Died',null=True,blank=True)
    

    def __str__(self):
        return '%s (%s)' %(self.apellido,self.nombre)