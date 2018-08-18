from django.test import TestCase
from taquillaAPI.models import *

class TaquillaTestCase(TestCase):
	def setUp(self):
		pass


def cliente_crear_test(self):
	cliente1 = Cliente(cedula='V21759474',
		nombre = 'José',
		apellido = 'Basanta',
		telefono = '04241642685')
	cliente1.save()
