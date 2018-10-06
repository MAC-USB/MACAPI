from django.shortcuts import render
from taquillaAPI.models import *
from taquillaAPI.models import PlataformaPago
from taquillaAPI.serializers import *
from rest_framework import generics

# Create your views here.

"""

Views del Restframework

"""

class ArticuloList(generics.ListCreateAPIView):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloSerializer

class ArticuloUpdate(generics.UpdateAPIView):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloSerializer

class ArticuloDestroy(generics.DestroyAPIView):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloSerializer

class ClienteList(generics.ListCreateAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	

class ClienteUpdate(generics.UpdateAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	lookup_field = 'cedula'

class ClienteDestroy(generics.DestroyAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	lookup_field = 'cedula'

class InteresList(generics.ListCreateAPIView):
	queryset = Interes.objects.all()
	serializer_class = InteresSerializer	

class PreparadorList(generics.ListCreateAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorSerializer

class HistorialCuentaList(generics.ListCreateAPIView):
	queryset = HistorialCuenta.objects.all()
	serializer_class = HistorialCuentaSerializer

class PlataformaPagoList(generics.ListCreateAPIView):
	queryset = PlataformaPago.objects.all()
	serializer_class = PlataformaPagoSerializer

class TransaccionList(generics.ListCreateAPIView):
	queryset = Transaccion.objects.all()
	serializer_class = TransaccionSerializer

class VentaList(generics.ListCreateAPIView):
	queryset = Venta.objects.all()
	serializer_class = VentaSerializer

class DeudaList(generics.ListCreateAPIView):
	queryset = Deuda.objects.all()
	serializer_class = DeudaSerializer

class PagoDeudaList(generics.ListCreateAPIView):
	queryset = PagoDeuda.objects.all()
	serializer_class = PagoDeudaSerializer

