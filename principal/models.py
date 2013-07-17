#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Bebida(models.Model):
	nombre = models.CharField(max_length=50)
	ingredientes = models.TextField()
	preparacion = models.TextField()

	def __unicode__(self):
		return self.nombre
		
class Receta(models.Model):
	#Dato cadena, longitud máxima 100 y único
	titulo = models.CharField(max_length=100, unique=True)
	#Dato texto, con texto de ayuda
	ingredientes = models.TextField(help_text='Redacta los ingredientes')
	#Dato texto, con nombre: Preparación
	preparacion = models.TextField(verbose_name='Preparacion')
	#Dato imagen, se almacenarán en la carpeta recetas, titulo: Imágen
	imagen = models.ImageField(upload_to='recetas', verbose_name='Imagen')
	#Dato Fecha y Hora, almacena la fecha actual
	tiempo_registro = models.DateTimeField(auto_now=True)
	#Enlace al modelo Usuario que Django ya tiene construido
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.titulo
		