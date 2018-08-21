from rest_framework import serializers
from taquillaAPI.models import *

"""
 Serializers para hacer funcionar el Rest framework
"""


class ArticuloSerializer(serializers.ModelSerializer):

	"""
	Consiste en el serializer del modelo Articulo.

	Campos que se van a pasar: nombre, precio
	"""
	class Meta:
		model = Articulo
		fields = ('nombre','precio')

class ClienteSerializer(serializers.ModelSerializer):
	"""
	Consiste en el serializer del modelo Cliente.

	Campos que se van a pasar: nombre, precio
	"""
	class Meta:
		model = Cliente
		fields = ('cedula', 'nombre','apellido','telefono')


class InteresSerializer(serializers.ModelSerializer):
	"""
	Consiste en el serializer del modelo Cliente.

	Campos que se van a pasar: porcentaje, rango_dias
	"""
	class Meta:
		model = Interes
		fields = ('porcentaje', 'rango_dias')

class PreparadorSerializer(serializers.ModelSerializer):
	"""
	Consiste en el serializer del modelo Preparador.

	Campos que se van a pasar: cedula, iniciales, nombre, apellido, correo, cantidad_deuda, fecha_deuda
	"""
	class Meta:
		model = Preparador
		fields = ('cedula', 'iniciales','nombre','apellido','cantidad_deuda','fecha_deuda')

class HistorialCuentaSerializer(serializers.ModelSerializer):
	"""
	Consiste en el serializer del modelo HistorialCuenta.

	Campos que se van a pasar: fecha, cant_ideal_efectivo, cant_ideal_caja, cant_real_efectivo,cant_real_caja
	"""
	class Meta:
		model = HistorialCuenta
		fields = ('fecha','cant_ideal_efectivo','cant_ideal_caja','cant_real_efectivo','cant_real_caja')

class PlataformaPagoSerializer(serializers.ModelSerializer):
	"""
	Consiste en el serializer del modelo PlataformaPago

	Campos que se van a pasar: nombre
	"""
	class Meta:
		model = PlataformaPago
		fields = ['nombre'] 

class TransaccionSerializer(serializers.ModelSerializer):
	"""
	Consiste en el serializer del modelo Transaccion.

	Campos que se van a pasar: fecha, monto, tipo
	"""
	class Meta:
		model = Transaccion
		fields = ('fecha','monto')

class VentaSerializer(serializers.ModelSerializer):
	"""
	Consiste en el serializer del modelo Venta.

	Campos que se van a pasar: id_transaccion, cantidad_producto, articulo, tipoPago, nro_confirmacion, plataforma_pago, cliente, preparador
	"""
	class Meta:
		model = Venta
		fields = ('id_transaccion','cantidad_producto','articulo','tipoPago','nro_confirmacion','plataforma_pago','cliente','preparador')

class DeudaSerializer(serializers.ModelSerializer):
	"""
	Consiste en el serializer del modelo Deuda.

	Campos que se van a pasar: id_transaccion, articulo, cantidad_producto, preparador
	"""
	class Meta:
		model = Deuda
		fields = ('id_transaccion','articulo','cantidad_producto','preparador')

class PagoDeudaSerializer(serializers.ModelSerializer):
	"""
	Consiste en el serializer del modelo PagoDeuda.

	Campos que se van a pasar: id_transaccion, montoDeuda, tipoPago, nro_confirmacion, plataforma_pago, fecha_pago, preparador
	"""
	class Meta:
		model = PagoDeuda
		fields = ('id_transaccion','montoDeuda','tipoPago','nro_confirmacion','plataforma_pago','fecha_pago','preparador')