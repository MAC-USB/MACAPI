from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from datetime import datetime

class Articulo(models.Model):
	"""
	Consiste en la tabla de las asignaturas.

	Parametros:
		models.Model (Articulo): es la instancia sobre la que se crea la tabla.

	Atributos de la clase:
		nombre: Nombre del articulo.
		precio: Precio del articulo.
	"""
	nombre = models.CharField(max_length=50,validators=[RegexValidator(regex='[a-zA-Z]',message='Nombre invalido')])
	precio = models.FloatField(default=0)

	def __str__(self):
    		return str(self.nombre)
	
class Cliente(models.Model):
	"""
	Consiste en la tabla de clientes.

	Parametros:
		models.Model (Cliente): es la instancia sobre la que se crea la tabla.

	Atributos de la clase:
		cedula: La cedula del cliente.
		nombre: El nombre del cliente.
		apellido: El apellido del cliente.
		telefono: El Telefono del cliente.
	"""
	cedula = models.CharField(primary_key=True, max_length=10,validators=[RegexValidator(regex="^[V|E|J|P]\-[0-9]{5,8}$",message="Cedula invalida")])
	nombre = models.CharField(max_length=50,validators=[RegexValidator(regex="^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$",message='Nombre invalido')])
	apellido = models.CharField(max_length=50,validators=[RegexValidator(regex="^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$",message='Apellido invalido')])
	telefono = models.CharField(max_length=15,validators=[RegexValidator(regex="[(]?\d{3}[)]?\s?-?\s?\d{3}\s?-?\s?\d{4}",message='Telefono invalido')])

	def __str__(self):
    		return str(self.cedula)
class Interes(models.Model):
	"""
	Consiste en la tabla de intereses.

	Parametros:
		models.Model (Interes): es la instancia sobre la que se crea la tabla.

	Atributos de la clase:
		porcentaje: Es el porcentaje del interes.
		rango_dias: Es la cantidad de dias que corresponde a ese interes.
	"""
	porcentaje = models.FloatField(default=0)
	rango_dias = models.IntegerField(default=0)

	def __str__(self):
    		return str(self.porcentaje)
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
	cedula = models.CharField(primary_key=True, max_length=10,validators=[RegexValidator(regex="^[V|E|J|P]\-[0-9]{5,8}$",message="Cedula invalida")])
	iniciales = models.CharField(default=None,max_length=3,validators=[RegexValidator(regex='[A-Z]{2,3}',message='Iniciales inválidas')])
	nombre = models.CharField(max_length=50,validators=[RegexValidator(regex='[a-zA-Z]+',message='Nombre invalido')])
	apellido = models.CharField(max_length=50,validators=[RegexValidator(regex='[a-zA-Z]+',message='Apellido invalido')])
	correo = models.EmailField(max_length=20,null=True,blank=True,validators=[RegexValidator(regex='([a-zA-Z0-9_-]+\.?){1,}@[a-z]+\.[a-z]{1,}', message='Email invalido')])
	cantidad_deuda = models.FloatField(default=0)
	fecha_deuda = models.DateTimeField(default=None,null=True)

	def __str__(self):
			return str(self.iniciales)

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
	cant_ideal_efectivo = models.FloatField(default=0)
	cant_ideal_caja = models.FloatField(default=0)
	cant_real_efectivo = models.FloatField(default=0)
	cant_real_caja = models.FloatField(default=0)

	def __str__(self):
    		return str(self.fecha)

class PlataformaPago(models.Model):
	"""
	Consiste en la tabla de plataformas de pago usadas para una transaccion.

	Parametros:
		models.Model (Cliente): es la instancia sobre la que se crea la tabla.

	Atributos de la clase:
		nombre: La denominacion de la plataforma de pago.
	"""
	nombre = models.CharField(max_length=30,validators=[RegexValidator(regex='[a-zA-Z]+',message='Nombre invalido')])
	codigo_banco = models.IntegerField(validators=[MaxValueValidator(9999)],null=True)
	
	def __str__(self):
    		return str(self.nombre)

class Transaccion(models.Model):
	"""
	Consiste en la tabla de transacciones de taquilla.

	Parametros:
		models.Model (Cliente): es la instancia sobre la que se crea la tabla.

	Atributos de la clase:
		fecha  : Fecha del cierre de caja por el sistema.
		monto  : Atributo derivado que indica el valor de la transaccion.
		tipo   : Indica el tipo de la transaccion (en discusion).
	"""
	fecha = models.DateTimeField(default=datetime.now)
	monto = models.FloatField(default=None)
	tipo = models.CharField(max_length=30,null=True,validators=[RegexValidator(regex='[a-zA-Z]+',message='Tipo invalido')])

	def __str__(self):
    		return str(self.fecha)

class Venta(models.Model):
	"""
	Se trata de una subclase de Transaccion, y consiste en las ventas por
	taquilla.

	Parametros:
		models.Model (Cliente): es la instancia sobre la que se crea la tabla.

	Atributos de la clase:
		id_transaccion : Referencia a la tabla transaccion, su superclase.
		articulo : Referencia al articulo solicitado.
		cantidad_producto : Cantidad del producto solicitado.
		tipoPago : Tipo de pago, transferencia o efectivo.
		nro_confirmacion : numero de confirmacion, en caso de ser tranferencia.
		plataforma_pago : Referencia a la plataforma de pago utilizada, de ser
						  transferencia.
		cliente : Referencia al cliente.
		preparador : Referencia al preparador.
		notas : Anotaciones referentes a la venta en particular (en discusion).
	"""
	id_transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
	cantidad_producto = models.IntegerField(default=0)
	articulo = models.ForeignKey(Articulo,on_delete=models.CASCADE)
	tipoPago = models.CharField(max_length=30,validators=[RegexValidator(regex='[a-zA-Z]+',message='Tipo invalido')])
	nro_confirmacion = models.IntegerField(default=None)
	plataforma_pago = models.ForeignKey(PlataformaPago, on_delete=models.CASCADE,default=None)
	cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
	preparador = models.ForeignKey(Preparador,on_delete=models.CASCADE)
	notas = models.CharField(max_length=60,null=True)


class Deuda(models.Model):
	"""
	Se trata de una subclase de Transaccion, y consiste en el registro de deuda por
	parte de los preparadores al adquirir algun producto.

	Parametros:
		models.Model (Cliente): es la instancia sobre la que se crea la tabla.

	Atributos de la clase:
		id_transaccion : Referencia a la tabla transaccion, su superclase.
		articulo : Referencia al articulo solicitado.
		cantidad_producto : Cantidad del producto solicitado.
		preparador : Referencia al preparador.
	"""
	id_transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
	articulo = models.ForeignKey(Articulo,on_delete=models.CASCADE)
	cantidad_producto = models.IntegerField(default=0)
	preparador = models.ForeignKey(Preparador,on_delete=models.CASCADE)

class PagoDeuda(models.Model):
	"""
	Se trata de una subclase de Transaccion, y consiste en pagos de la deuda
	acumulada de un preparador.

	Parametros:
		models.Model (Cliente): es la instancia sobre la que se crea la tabla.

	Atributos de la clase:
		id_transaccion : Referencia a la tabla transaccion, su superclase.
		montoDeuda : Cantidad del producto solicitado.
		tipoPago : Tipo de pago, transferencia o efectivo.
		nro_confirmacion : numero de confirmacion, en caso de ser tranferencia.
		plataforma_pago : Referencia a la plataforma de pago utilizada, de ser
						  transferencia.
		fecha_pago : En caso de ser transferencia, fecha de realizacion de la misma.
		preparador : Referencia al preparador.
	"""
	id_transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
	montoDeuda = models.FloatField(default=0)
	tipoPago = models.CharField(max_length=30,validators=[RegexValidator(regex='[a-zA-Z]')])
	nro_confirmacion = models.IntegerField(default=None)
	plataforma_pago = models.ForeignKey(PlataformaPago, on_delete=models.CASCADE, default=None)
	fecha_pago = models.DateTimeField(default=datetime.now)
	preparador = models.ForeignKey(Preparador,on_delete=models.CASCADE)
