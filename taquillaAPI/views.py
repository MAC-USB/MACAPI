from django.shortcuts import render
from taquillaAPI.models import *
from taquillaAPI.serializers import *
from rest_framework import generics

# Create your views here.

"""

Views of Restframework

"""

class ProductListCreate(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class ClientListCreate(generics.ListCreateAPIView):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer

class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Client.objects.all()
	serializer_class = ClientUpdateSerializer
	lookup_field = 'id_document'

class InterestListCreate(generics.ListCreateAPIView):
	queryset = Interest.objects.all()
	serializer_class = InterestSerializer

class InterestRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Interest.objects.all()
	serializer_class = InterestSerializer

class AssistantListCreate(generics.ListCreateAPIView):
	queryset = Assistant.objects.all()
	serializer_class = AssistantSerializer

class AssistantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Assistant.objects.all()
	serializer_class = AssistantUpdateSerializer
	lookup_field = 'id_document'

class AccountHistoryListCreate(generics.ListCreateAPIView):
	queryset = AccountHistory.objects.all()
	serializer_class = AccountHistorySerializer

class AccountHistoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = AccountHistory.objects.all()
	serializer_class = AccountHistoryUpdateSerializer
	lookup_field = 'date'

class BankListCreate(generics.ListCreateAPIView):
	queryset = Bank.objects.all()
	serializer_class = BankSerializer

class BankRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Bank.objects.all()
	serializer_class = BankSerializer

class PayMethodListCreate(generics.ListCreateAPIView):
	queryset = PayMethod.objects.all()
	serializer_class = PayMethodSerializer

class PayMethodRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = PayMethod.objects.all()
	serializer_class = PayMethodSerializer

class TransactionListCreate(generics.ListCreateAPIView):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

class TransactionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer


class SaleListCreate(generics.ListCreateAPIView):
	queryset = Sale.objects.all()

	def get_serializer_class(self):
		method = self.request.method
		if method == 'GET':
			return SaleDetailsSerializer
		else:
			return SaleSerializer

class SaleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer

	def get_serializer_class(self):
		method = self.request.method
		if method == 'PUT':
			return SaleSerializer
		else:
			return SaleDetailsSerializer

class DebtListCreate(generics.ListCreateAPIView):
	queryset = Debt.objects.all()
	serializer_class = DebtSerializer

class DebtRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Debt.objects.all()
	serializer_class = DebtSerializer


class DebtPaymentListCreate(generics.ListCreateAPIView):
	queryset = DebtPayment.objects.all()
	serializer_class = DebtPaymentSerializer

	def get_serializer_class(self):
		method = self.request.method
		if method == 'GET':
			return DebtPaymentDetailsSerializer
		else:
			return DebtPaymentSerializer

class DebtPaymentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = DebtPayment.objects.all()
	serializer_class = DebtPaymentSerializer

	def get_serializer_class(self):
		method = self.request.method
		if method == 'PUT':
			return DebtPaymentSerializer
		else:
			return DebtPaymentDetailsSerializer

class ItemListCreate(generics.ListCreateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

	def get_serializer_class(self):
		method = self.request.method
		if method == 'GET':
			return ItemDetailsSerializer
		else:
			return ItemSerializer

class ItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

	def get_serializer_class(self):
		method = self.request.method
		if method == 'PUT':
			return ItemSerializer
		else:
			return ItemDetailsSerializer
