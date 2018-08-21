from rest_framework import serializers
from taquillaAPI.models import Articulo

class ArticuloSerializer(serializers.ModelSerializer):
	class Meta:
		model = Articulo
		fields = ('nombre','precio')