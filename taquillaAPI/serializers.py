from rest_framework import serializers
from taquillaAPI.models import *

"""
 Serializers to make works the Rest framework
"""


class ProductSerializer(serializers.ModelSerializer):

	"""
	Consist in the serializer of model Product.

	Fields that are going to pass: name, price
	"""
	class Meta:
		model = Product
		fields = ('pk','name','price')

class ClientSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model Client.

	Fields that are going to pass: first_name, price
	"""
	class Meta:
		model = Client
		fields = ('id_document', 'first_name','last_name','phone_number')

class ClientUpdateSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializerr update of model Client.

	Fields that are going to pass: first_name, last_name, phone_number
	Fields that are read only: id_document
	"""
	class Meta:
		model = Client
		fields = ('id_document', 'first_name','last_name','phone_number')
		read_only_fields = ('id_document',)

class InterestSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model Interest.

	Fields that are going to pass: percentage, range_days
	"""
	class Meta:
		model = Interest
		fields = ('pk','percentage', 'range_days')

class AssistantSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model Assistant.

	Fields that are going to pass: id_document, initials, first_name, last_name, email, debt_amount, debt_date
	"""
	class Meta:
		model = Assistant
		fields = ('id_document', 'initials','first_name','last_name','debt_amount','debt_date','email')

class AssistantUpdateSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializerr update of model Assistant.

	Fields that are going to pass: id_document, initials, first_name, last_name, email, debt_amount, debt_date
	Fields that are read only: id_document
	"""
	class Meta:
		model = Assistant
		fields = ('id_document', 'initials','first_name','last_name','debt_amount','debt_date','email')
		read_only_fields = ('id_document',)

class AccountHistorySerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model AccountHistory.

	Fields that are going to pass: date, ideal_amount_cash, ideal_amount_account, real_amount_cash,real_amount_account
	"""
	class Meta:
		model = AccountHistory
		fields = ('date','ideal_amount_cash','ideal_amount_account','real_amount_cash','real_amount_account')

class AccountHistoryUpdateSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializerr update of model AccountHistory.

	Fields that are going to pass: date, ideal_amount_cash, ideal_amount_account, real_amount_cash,real_amount_account
	Fields that are read only: date
	"""
	class Meta:
		model = Client
		fields = ('date','ideal_amount_cash','ideal_amount_account','real_amount_cash','real_amount_account')
		read_only_fields = ('date',)

class BankSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model Bank

	Fields that are going to pass: name,code
	"""
	class Meta:
		model = Bank
		fields = ('pk','name','code') 


class TransactionSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model Transaction.

	Fields that are going to pass: date, amount, types
	"""
	class Meta:
		model = Transaction
		fields = ('pk','date','amount','types')


#Serializer mixed

class AssistantDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Assistant
		fields = ('pk','initials')

class ClientDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = ('pk','first_name', 'last_name')

class PayMethodSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model PayMethod

	Fields that are going to pass: description
	"""
	class Meta:
		model = PayMethod
		fields = ('description',)
		
class BankDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bank
		fields = ('pk','name','code')

class ProductDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('pk','name' )	

class SaleSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model Sale.

	Fields that are going to pass: transaction, product_quantity, product, pay_method, confirmation_no, bank, client, assistant
	"""

	class Meta:
		model = Sale
		fields = ('pk','transaction','product_quantity','product','pay_method','confirmation_no','bank','client','assistant','notes')

class SaleDetailsSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model Sale.

	Fields that are going to pass: transaction, product_quantity, product, pay_method, confirmation_no, bank, client, assistant
	"""
	assistant = AssistantDetailsSerializer()
	client = ClientDetailsSerializer()
	pay_method = PayMethodSerializer()
	bank = BankDetailsSerializer()
	product = ProductDetailsSerializer()

	class Meta:
		model = Sale
		fields = ('pk','transaction','product_quantity','product','pay_method','confirmation_no','bank','client','assistant','notes')

class DebtSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model Debt.

	Fields that are going to pass: transaction, product, product_quantity, assistant
	"""
	class Meta:
		model = Debt
		fields = ('pk','transaction','product','product_quantity','assistant')

class DebtPaymentSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model DebtPayment.

	Fields that are going to pass: transaction, debt_amount, pay_method, confirmation_no, bank, pay_date, assistant
	"""
	class Meta:
		model = DebtPayment
		fields = ('pk','transaction','debt_amount','pay_method','confirmation_no','bank','pay_date','assistant')