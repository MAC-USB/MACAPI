from django.shortcuts import render
from taquillaAPI.models import Articulo
from taquillaAPI.serializers import ArticuloSerializer
from rest_framework import generics

# Create your views here.

class ArticuloList(generics.ListCreateAPIView):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloSerializer