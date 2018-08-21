from django import forms
from django.forms import ModelForm
from .models import *
from django.core.exceptions import NON_FIELD_ERRORS

""" En el presente archivo se presentan los forms de todas las
tablas en la base de datos para esta aplicacion.
"""

class ArticuloForm(ModelForm):
    """ Form para añadir una instancia a la tabla de articulos.
    """
    class Meta:
        model = Articulo
        fields = ["nombre", "precio"]

class ClienteForm(ModelForm):
    """ Form para añadir una instancia a la tabla de clientes.
    """
    class Meta:
        model = Cliente
        fields = ["cedula","nombre", "apellido","telefono"]

class InteresForm(ModelForm):
    """ Form para añadir una instancia a la tabla de intereses.
    """
    class Meta:
        model = Interes
        fields = ["porcentaje","rango_dias"]

class PreparadorForm(ModelForm):
    """ Form para añadir una instancia a la tabla de preparadores.
    """
    class Meta:
        model = Preparador
        fields = ["cedula","iniciales","nombre", "apellido","cantidad_deuda","fecha_deuda"]

class HistorialCuentaForm(ModelForm):
    """ Form para añadir una instancia a la tabla de historial de cuenta.
    """
    class Meta:
        model = HistorialCuenta
        fields = ["fecha", "cant_ideal_efectivo","cant_ideal_caja","cant_real_efectivo","cant_real_caja"]

class PlataformaPagoForm(ModelForm):
    """ Form para añadir una instancia a la tabla de plataforma de pago.
    """
    class Meta:
        model = PlataformaPago
        fields = ["nombre"]

class TransaccionForm(ModelForm):
    """ Form para añadir una instancia a la tabla de transacciones.
    """
    class Meta:
        model = Transaccion
        fields = ["fecha","monto"]

class VentaForm(ModelForm):
    """ Form para añadir una instancia a la tabla de ventas, subclase de Transaccion.
    """
    class Meta:
        model = Venta
        fields = ["id_transaccion",
                "cantidad_producto",
                "articulo",
                "tipoPago",
                "nro_confirmacion",
                "plataforma_pago",
                "cliente",
                "preparador"
                ]

class DeudaForm(ModelForm):
    """ Form para añadir una instancia a la tabla de Deudas, subclase de Transaccion.
    """
    class Meta:
        model = Deuda
        fields = ["id_transaccion",
                "articulo",
                "cantidad_producto",
                "preparador"
                ]

class PagoDeudaForm(ModelForm):
    """ Form para añadir una instancia a la tabla de Pago de deudas, subclase de
    Transaccion.
    """
    class Meta:
        model = PagoDeuda
        fields = ["id_transaccion",
                "montoDeuda",
                "tipoPago",
                "nro_confirmacion",
                "plataforma_pago",
                "fecha_pago",
                "preparador",
                ]