from django.shortcuts import render
from taquillaAPI.models import *
from taquillaAPI.serializers import *
from rest_framework import generics
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

# Create your views here.

"""

Views of Restframework

"""


class ProductListCreate(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(ProductListCreate, self).dispatch(*args, **kwargs)


class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(ProductRetrieveUpdateDestroy, self).dispatch(*args, **kwargs)

class ClientListCreate(generics.ListCreateAPIView):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(ClientListCreate, self).dispatch(*args, **kwargs)

class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Client.objects.all()
	serializer_class = ClientUpdateSerializer
	lookup_field = 'id_document'
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(ClientRetrieveUpdateDestroy, self).dispatch(*args, **kwargs)

class InterestListCreate(generics.ListCreateAPIView):
	queryset = Interest.objects.all()
	serializer_class = InterestSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(InterestListCreate, self).dispatch(*args, **kwargs)

class InterestRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Interest.objects.all()
	serializer_class = InterestSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(InterestRetrieveUpdateDestroy, self).dispatch(*args, **kwargs)

class AssistantListCreate(generics.ListCreateAPIView):
	queryset = Assistant.objects.all()
	serializer_class = AssistantSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(AssistantListCreate, self).dispatch(*args, **kwargs)

class AssistantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Assistant.objects.all()
	serializer_class = AssistantUpdateSerializer
	lookup_field = 'id_document'
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(AssistantRetrieveUpdateDestroy, self).dispatch(*args, **kwargs)

class AccountHistoryListCreate(generics.ListCreateAPIView):
	queryset = AccountHistory.objects.all()
	serializer_class = AccountHistorySerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(AccountHistoryListCreate, self).dispatch(*args, **kwargs)

class AccountHistoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = AccountHistory.objects.all()
	serializer_class = AccountHistoryUpdateSerializer
	lookup_field = 'date'
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(AccountHistoryRetrieveUpdateDestroy, self).dispatch(*args, **kwargs)

class BankListCreate(generics.ListCreateAPIView):
	queryset = Bank.objects.all()
	serializer_class = BankSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(BankListCreate, self).dispatch(*args, **kwargs)

class BankRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Bank.objects.all()
	serializer_class = BankSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(BankRetrieveUpdateDestroy, self).dispatch(*args, **kwargs)

class PayMethodListCreate(generics.ListCreateAPIView):
	queryset = PayMethod.objects.all()
	serializer_class = PayMethodSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(PayMethodListCreate, self).dispatch(*args, **kwargs)

class PayMethodRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = PayMethod.objects.all()
	serializer_class = PayMethodSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(PayMethodRetrieveUpdateDestroy, self).dispatch(*args, **kwargs)

class TransactionListCreate(generics.ListCreateAPIView):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(TransactionListCreate, self).dispatch(*args, **kwargs)

class TransactionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(TransactionRetrieveUpdateDestroy, self).dispatch(*args, **kwargs)


class SaleListCreate(generics.ListCreateAPIView):
	queryset = Sale.objects.all()

	def get_serializer_class(self):
		method = self.request.method
		if method == 'GET':
			return SaleDetailsSerializer
		else:
			return SaleSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(SaleListCreate, self).dispatch(*args, **kwargs)

class SaleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer

	def get_serializer_class(self):
		method = self.request.method
		if method == 'PUT':
			return SaleSerializer
		else:
			return SaleDetailsSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(SaleRetrieveUpdateDestroy, self).dispatch(*args, **kwargs)

class DebtListCreate(generics.ListCreateAPIView):
	queryset = Debt.objects.all()
	serializer_class = DebtSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(DebtListCreate, self).dispatch(*args, **kwargs)

class DebtRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Debt.objects.all()
	serializer_class = DebtSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(DebtRetrieveUpdateDestroy, self).dispatch(*args, **kwargs)


class DebtPaymentListCreate(generics.ListCreateAPIView):
	queryset = DebtPayment.objects.all()
	serializer_class = DebtPaymentSerializer

	def get_serializer_class(self):
		method = self.request.method
		if method == 'GET':
			return DebtPaymentDetailsSerializer
		else:
			return DebtPaymentSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(DebtPaymentListCreate, self).dispatch(*args, **kwargs)

class DebtPaymentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = DebtPayment.objects.all()
	serializer_class = DebtPaymentSerializer

	def get_serializer_class(self):
		method = self.request.method
		if method == 'PUT':
			return DebtPaymentSerializer
		else:
			return DebtPaymentDetailsSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(DebtPaymentRetrieveUpdateDestroy, self).dispatch(*args, **kwargs)

class ItemListCreate(generics.ListCreateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

	def get_serializer_class(self):
		method = self.request.method
		if method == 'GET':
			return ItemDetailsSerializer
		else:
			return ItemSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(ItemListCreate, self).dispatch(*args, **kwargs)

class ItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

	def get_serializer_class(self):
		method = self.request.method
		if method == 'PUT':
			return ItemSerializer
		else:
			return ItemDetailsSerializer
	@method_decorator(login_required(login_url='/admin/'))
	def dispatch(self, *args, **kwargs):
		return super(ItemRetrieveUpdateDestroy, self).dispatch(*args, **kwargs)
