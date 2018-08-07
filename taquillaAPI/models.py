from django.db import models

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
    cantidad_deuda = models.IntegerField()
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
    cant_efectivo = models.IntegerField()
    cant_caja = models.IntegerField()
    id_transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
