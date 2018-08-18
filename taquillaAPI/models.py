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
		apellido: El apellido del cliente.
		telefono: El Telefono del cliente.
	"""
	cedula = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
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
        nombre : Nombre del preparador.
		apellido : apellido del preparador.
        correo : Correo asociado.
        cantidad_deuda : Cantidad de deuda acumulada.
        fecha_deuda : Fecha en la cual cantidad_deuda pasó a ser mayor de cero. Default
                      es None.
	"""
    cedula = models.IntegerField(primary_key=True)
    iniciales = models.CharField(default=None,max_length=3)
    nombre = models.CharField(max_length=50,validators=[RegexValidator(regex='[a-zA-Z]+',message='Nombre invalido')])
	apellido = models.CharField(max_length=50,validators=[RegexValidator(regex='[a-zA-Z]+',message='Nombre invalido')])
    correo = models.CharField(max_length=20,validators=[RegexValidator(regex='([a-zA-Z0-9_-]+\.?){1,}@[a-z]+\.[a-z]{1,}', message='Email invalido')])
    cantidad_deuda = models.FloatField(default=0)
    fecha_deuda = models.DateTimeField(default=None)

class HistorialCuenta(models.Model):
    """
    Tabla que almacena los preparadores activos o recurrentes.
	
    Parametros:
		models.Model (Coordinacion): es la instancia sobre la que se crea la tabla.
	
    Atributos de la clase: 
		fecha  : Clave primaria. Fecha del cierre de caja por el sistema.
		cant_ideal_efectivo  :  Cantidad en efectivo calculada por el sistema a partir
								de las ventas de la fecha.
		cant_ideal_caja  :  Cantidad en banco calculada por el sistema a partir
							de las ventas de la fecha.
		cant_ideal_efectivo  :  Cantidad en efectivo indicada por el preparador en
								la fecha.
		cant_ideal_caja  :  Cantidad en banco indicada por el preparador en la fecha.
        fecha : fecha de la transaccion asociada que produjo un cambio.
	"""
	fecha = models.DateTimeField(primary_key=True)
	cant_ideal_efectivo = models.FloatField()
    cant_ideal_caja = models.FloatField()
    cant_real_efectivo = models.FloatField(default=0)
    cant_real_caja = models.FloatField(default=0)
	
    
