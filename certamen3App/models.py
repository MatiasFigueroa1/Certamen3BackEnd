from django.db import models


class Marca(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.CharField(max_length=50)
    año = models.CharField(max_length=200)
    gama = models.CharField(max_length=100)



class Auto(models.Model):
    marca = models.ForeignKey(Marca)
    modelo = models.CharField(max_length=200)
    año = models.CharField(max_length=15)
    image = models.ImageField(upload_to='media/')

    
