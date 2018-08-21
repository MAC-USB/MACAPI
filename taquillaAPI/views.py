from django.shortcuts import render
from taquillaAPI.models import *
from taquillaAPI.serializers import *
from rest_framework import generics

# Create your views here.

"""

Views del Restframework

"""

class ArticuloList(generics.ListCreateAPIView):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloSerializer

class ClienteList(generics.ListCreateAPIView):
	queryset = Cliente.objects.all()
	serializers_class = ClienteSerializer

class InteresList(generics.ListCreateAPIView):
	queryset = Interes.objects.all()
	serializers_class = InteresSerializer	

class PreparadorList(generics.ListCreateAPIView):
	queryset = Preparador.objects.all()
	serializers_class = PreparadorSerializer

class HistorialCuentaList(generics.ListCreateAPIView):
	queryset = HistorialCuenta.objects.all()
	serializers_class = HistorialCuentaSerializer

"""
class PlataformaPagoList(generics.ListCreateAPIView):
	queryset = PlataformaPago.objects.all()
	serializers_class = PlataformaPagoSerializer

class TransaccionList(generics.ListCreateAPIView):
	queryset = Transaccion.objects.all()
	serializers_class = TransaccionSerializer

class VentaList(generics.ListCreateAPIView):
	queryset = Venta.objects.all()
	serializers_class = VentaSerializer

class DeudaList(generics.ListCreateAPIView):
	queryset = Deuda.objects.all()
	serializers_class = DeudaSerializer

class PagoDeudaList(generics.ListCreateAPIView):
	queryset = PagoDeuda.objects.all()
	serializers_class = PagoDeudaSerializer
"""
