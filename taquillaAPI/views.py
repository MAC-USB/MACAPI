from django.shortcuts import render
from taquillaAPI.models import *
from taquillaAPI.models import PlataformaPago
from taquillaAPI.serializers import *
from rest_framework import generics

# Create your views here.

"""

Views del Restframework

"""

class ArticuloListCreate(generics.ListCreateAPIView):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloSerializer

class ArticuloRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloSerializer

class ClienteListCreate(generics.ListCreateAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer

class ClienteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteUpdateSerializer
	lookup_field = 'cedula'

class InteresListCreate(generics.ListCreateAPIView):
	queryset = Interes.objects.all()
	serializer_class = InteresSerializer

class InteresRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Interes.objects.all()
	serializer_class = InteresSerializer

class PreparadorListCreate(generics.ListCreateAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorSerializer

class PreparadorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorUpdateSerializer
	lookup_field = 'cedula'

class HistorialCuentaListCreate(generics.ListCreateAPIView):
	queryset = HistorialCuenta.objects.all()
	serializer_class = HistorialCuentaSerializer

class HistorialCuentaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = HistorialCuenta.objects.all()
	serializer_class = HistorialCuentaUpdateSerializer
	lookup_field = 'fecha'

class PlataformaPagoListCreate(generics.ListCreateAPIView):
	queryset = PlataformaPago.objects.all()
	serializer_class = PlataformaPagoSerializer

class PlataformaPagoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = PlataformaPago.objects.all()
	serializer_class = PlataformaPagoSerializer

class TransaccionListCreate(generics.ListCreateAPIView):
	queryset = Transaccion.objects.all()
	serializer_class = TransaccionSerializer

class TransaccionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Transaccion.objects.all()
	serializer_class = TransaccionSerializer


class VentaListCreate(generics.ListCreateAPIView):
	queryset = Venta.objects.all()
	serializer_class = VentaSerializer

class VentaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorSerializer


class DeudaListCreate(generics.ListCreateAPIView):
	queryset = Deuda.objects.all()
	serializer_class = DeudaSerializer

class DeudaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorSerializer


class PagoDeudaListCreate(generics.ListCreateAPIView):
	queryset = PagoDeuda.objects.all()
	serializer_class = PagoDeudaSerializer

class PagoDeudaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorSerializer

