from django.db import models
#si no carga las tablas en la base de datos usar:
#python manage.py makemigrations "certamen3App"

class Marca(models.Model):
    nombre = models.CharField(max_length=200, primary_key=True)
    pais = models.CharField(max_length=50)
    año = models.CharField(max_length=200)
    gama = models.CharField(max_length=100)



class Auto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, to_field='nombre')
    modelo = models.CharField(max_length=200)
    año = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/', default=None)
