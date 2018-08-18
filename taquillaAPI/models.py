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
    iniciales = models.CharField(default=None,max_length=3,validators=[RegexValidator(regex='[A-Z]{2,3}',message='Iniciales inválidas')])
    nombre = models.CharField(max_length=50,validators=[RegexValidator(regex='[a-zA-Z]+',message='Nombre invalido')])
	apellido = models.CharField(max_length=50,validators=[RegexValidator(regex='[a-zA-Z]+',message='Nombre invalido')])
    #correo = models.CharField(max_length=20,validators=[RegexValidator(regex='([a-zA-Z0-9_-]+\.?){1,}@[a-z]+\.[a-z]{1,}', message='Email invalido')])
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

class PlataformaPago(models.Model):
    """Consiste en la tabla de plataformas de pago usadas para una transaccion.

	Parametros:
		models.Model (Cliente): es la instancia sobre la que se crea la tabla.

	Atributos de la clase:
		nombre: La denominacion de la plataforma de pago.
	"""
	nombre = models.CharField()

class Transaccion(models.Model):
    """Consiste en la tabla de transacciones de taquilla.

	Parametros:
		models.Model (Cliente): es la instancia sobre la que se crea la tabla.

	Atributos de la clase:
		fecha  : Fecha del cierre de caja por el sistema.
		monto  : Atributo derivado que indica el valor de la transaccion.
		tipo   : Indica el tipo de la transaccion.
	"""
	fecha = models.DateTimeField()
	monto = models.FloatField(default=None)
	tipo = models.CharField()

class Venta(models.Model):
    """Se trata de una subclase de Transaccion, y consiste en las ventas por
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
		notas : Anotaciones referentes a la venta en particular.
	"""
	id_transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
	cantidad_producto = models.IntegerField(default=0)
	articulo = models.ForeignKey(Articulo)
	tipoPago = models.CharField()
	nro_confirmacion = models.IntegerField(default=None)
	plataforma_pago = models.ForeignKey(Banco, on_delete=models.CASCADE,default=None)
	cliente = models.ForeignKey(Cliente)
	preparador = models.ForeignKey(Preparador)
	notas = models.CharField()

class Deuda(models.Model):
    """Se trata de una subclase de Transaccion, y consiste en el registro de deuda por
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
	articulo = models.ForeignKey(Articulo)
	cantidad_producto = models.IntegerField(default=0)
	preparador = models.ForeignKey(Preparador)

class PagoDeuda(models.Model):
    """Se trata de una subclase de Transaccion, y consiste en pagos de la deuda
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
	tipoPago = models.CharField()
	nro_confirmacion = models.IntegerField(default=None)
	plataforma_pago = models.ForeignKey(Banco, on_delete=models.CASCADE, default=None)
	fecha_pago = models.DateTimeField(default=None)
	preparador = models.ForeignKey(Preparador)