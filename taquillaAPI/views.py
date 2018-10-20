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

class ArticuloRetrieve(generics.RetrieveAPIView):
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

class ClienteRetrieve(generics.RetrieveAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer

class ClienteUpdate(generics.UpdateAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteUpdateSerializer
	lookup_field = 'cedula'

class ClienteDestroy(generics.DestroyAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	lookup_field = 'cedula'

class InteresList(generics.ListCreateAPIView):
	queryset = Interes.objects.all()
	serializer_class = InteresSerializer

class InteresRetrieve(generics.RetrieveAPIView):
	queryset = Interes.objects.all()
	serializer_class = InteresSerializer

class InteresUpdate(generics.UpdateAPIView):
	queryset = Interes.objects.all()
	serializer_class = InteresSerializer


class InteresDestroy(generics.DestroyAPIView):
	queryset = Interes.objects.all()
	serializer_class = ClienteSerializer
		

class PreparadorList(generics.ListCreateAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorSerializer

class PreparadorRetrieve(generics.RetrieveAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorSerializer
	lookup_field = 'cedula'

class PreparadorUpdate(generics.UpdateAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorUpdateSerializer
	lookup_field = 'cedula'

class PreparadorDestroy(generics.DestroyAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorSerializer
	lookup_field = 'cedula'

class HistorialCuentaList(generics.ListCreateAPIView):
	queryset = HistorialCuenta.objects.all()
	serializer_class = HistorialCuentaSerializer

class HistorialCuentaRetrieve(generics.RetrieveAPIView):
	queryset = HistorialCuenta.objects.all()
	serializer_class = HistorialCuentaSerializer
	lookup_field = 'fecha'

class HistorialCuentaUpdate(generics.UpdateAPIView):
	queryset = HistorialCuenta.objects.all()
	serializer_class = HistorialCuentaUpdateSerializer
	lookup_field = 'cedula'

class HistorialCuentaDestroy(generics.DestroyAPIView):
	queryset = HistorialCuenta.objects.all()
	serializer_class = HistorialCuentaSerializer
	lookup_field = 'cedula'


class PlataformaPagoList(generics.ListCreateAPIView):
	queryset = PlataformaPago.objects.all()
	serializer_class = PlataformaPagoSerializer

class PlataformaPagoRetrieve(generics.RetrieveAPIView):
	queryset = PlataformaPago.objects.all()
	serializer_class = PlataformaPagoSerializer

class PlataformaPagoUpdate(generics.UpdateAPIView):
	queryset = PlataformaPago.objects.all()
	serializer_class = PlataformaPagoSerializer

class PlataformaPagoDestroy(generics.DestroyAPIView):
	queryset = PlataformaPago.objects.all()
	serializer_class = PlataformaPagoSerializer

class TransaccionList(generics.ListCreateAPIView):
	queryset = Transaccion.objects.all()
	serializer_class = TransaccionSerializer

class TransaccionRetrieve(generics.RetrieveAPIView):
	queryset = Transaccion.objects.all()
	serializer_class = TransaccionSerializer


class TransaccionUpdate(generics.UpdateAPIView):
	queryset = Transaccion.objects.all()
	serializer_class = TransaccionSerializer


class TransaccionDestroy(generics.DestroyAPIView):
	queryset = Transaccion.objects.all()
	serializer_class = TransaccionSerializer

class VentaList(generics.ListCreateAPIView):
	queryset = Venta.objects.all()
	serializer_class = VentaSerializer

class VentaRetrieve(generics.RetrieveAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorSerializer

class VentaUpdate(generics.UpdateAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorUpdateSerializer

class VentaDestroy(generics.DestroyAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorSerializer

class DeudaList(generics.ListCreateAPIView):
	queryset = Deuda.objects.all()
	serializer_class = DeudaSerializer

class DeudaRetrieve(generics.RetrieveAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorSerializer

class DeudaUpdate(generics.UpdateAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorUpdateSerializer

class DeudaDestroy(generics.DestroyAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorSerializer

class PagoDeudaList(generics.ListCreateAPIView):
	queryset = PagoDeuda.objects.all()
	serializer_class = PagoDeudaSerializer

class PagoDeudaRetrieve(generics.RetrieveAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorSerializer

class PagoDeudaUpdate(generics.UpdateAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorUpdateSerializer

class PagoDeudaDestroy(generics.DestroyAPIView):
	queryset = Preparador.objects.all()
	serializer_class = PreparadorSerializer

