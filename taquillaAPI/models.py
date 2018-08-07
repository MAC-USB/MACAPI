from django.db import models

class Articulo(models.Model):
	""" Consiste en la tabla de las asignaturas.

	Parametros:
		models.Model (Articulo): es la instancia sobre la que se crea la tabla.

	Atributos de la clase:
		nombre: Nombre del articulo.
		precio: Precio del articulo.
	"""
	nombre = models.CharField(max_length=50)
	precio = models.FloatField()
	
class Cliente(models.Model):

	"""Consiste en la tabla de clientes.

	Parametros:
		models.Model (Cliente): es la instancia sobre la que se crea la tabla.

	Atributos de la clase:
		cedula: La cedula del cliente.
		nombre: El nombre del cliente.
		telefono: El Telefono del cliente.
	"""
	cedula = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=50)
	telefono = models.CharField(max_length=15)

class Interes(models.Model):
	"""Consiste en la tabla de intereses.

	Parametros:
		models.Model (Interes): es la instancia sobre la que se crea la tabla.

	Atributos de la clase:
		porcentaje: Es el porcentaje del interes.
		rango_dias: Es la cantidad de dias que corresponde a ese interes.
	"""
	porcentaje = models.FloatField()
	rango_dias = models.IntegerField()
# Create your models here.
