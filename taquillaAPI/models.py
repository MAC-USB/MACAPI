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

class Preparador(models.Model):
    """
    Tabla que almacena los preparadores activos o recurrentes.
	
    Parametros:
		models.Model (Coordinacion): es la instancia sobre la que se crea la tabla.
	
    Atributos de la clase: 
		cedula : Cedula de identidad del preparador.
        iniciales : Iniciales del preparador, de tenerlas.
        nombre : Nombre completo del preparador.
        correo : Correo asociado.
        cantidad_deuda : Cantidad de deuda acumulada.
        fecha_deuda : Fecha en la cual cantidad_deuda pasó a ser mayor de cero. Default
                      es None.
	"""
    cedula = models.IntegerField(primary_key=True)
    iniciales = models.CharField(default=None,max_length=3)
    nombre = models.CharField()
    correo = models.CharField()
    cantidad_deuda = models.FloatField(default=0)
    fecha_deuda = models.DateTimeField(default=None)

class Bitacora(models.Model):
    """
    Tabla que almacena los preparadores activos o recurrentes.
	
    Parametros:
		models.Model (Coordinacion): es la instancia sobre la que se crea la tabla.
	
    Atributos de la clase: 
		cant_efectivo : Cantidad de dinero en efectivo en caja.
        cant_caja : Cantidad de dinero en la cuenta bancaria.
        fecha : fecha de la transaccion asociada que produjo un cambio.
	"""
    cant_efectivo = models.FloatField()
    cant_caja = models.FloatField()
    fecha_deuda = models.DateTimeField()
    id_transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
