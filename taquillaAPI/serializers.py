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

class PayMethodSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model PayMethod

	Fields that are going to pass: description
	"""
	class Meta:
		model = PayMethod
		fields = ('pk','description',)

class getTransactionSerializer(serializers.ModelSerializer):
    """
    Consist in the serializer of model Transaction.

    Fields that are going to pass: date, amount, pay_method, bank,
    reference_number, sale, debt_payment
    """
    bank = BankSerializer(read_only=True)
    pay_method = PayMethodSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = ('pk','date','amount','pay_method','bank', 'reference_number', 'sale', 'debt_payment')

class TransactionSerializer(serializers.ModelSerializer):
    """
    Consist in the serializer of model Transaction.

    Fields that are going to pass: date, amount, pay_method, bank,
    reference_number, sale, debt_payment
    """

    class Meta:
        model = Transaction
        fields = ('pk','date','amount','pay_method','bank', 'reference_number', 'sale', 'debt_payment')


#Serializer mixed

class AssistantDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Assistant
		fields = ('id_document','initials')

class ClientDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = ('id_document','first_name', 'last_name')

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

	Fields that are going to pass: date, item, client,
	assistant, notes
	"""

	class Meta:
		model = Sale
		fields = ('date','item', 'client','assistant','notes')

	#Override function create to save the sale correctly

	#  def create(self, validated_data):
    #     product_id = validated_data['product']
	# 	product_quantity = validated_data['product_quantity']
    #     product = Product.objects.filter(pk=product_id)
	# 	item_obj = Item(
	# 		product_id = product_id,
	# 		product_name = product.name,
	# 		product_price = product.price,
	# 		product_quantity = product_quantity
	# 	)
    #     item_obj.save()
    #     return validated_data


class ItemSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model Product.

	Fields that are going to pass: product_name, product_price, product_quantity
	"""

	product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
	class Meta:
		model = Item
		fields = ('pk','product_id','product_quantity' )

	def create(self, validated_data):
		product_id = validated_data['product_id']
		product_quantity = validated_data['product_quantity']
		product_name = product_id.name
		product_price = product_id.price
		item_obj = Item(
			product_id = product_id.pk,
			product_name = product_name,
			product_price = product_price,
			product_quantity = product_quantity
		)
		item_obj.save()

		return validated_data

	def update(self, instance, validated_data):
		product_id = validated_data['product_id']
		product_quantity = validated_data['product_quantity']
		product_name = product_id.name
		product_price = product_id.price
		instance.product_id = product_id.pk
		instance.product_quantity = product_quantity
		instance.product_name = product_name
		instance.product_price = product_price
		instance.save()
		return instance

class ItemDetailsSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model Product.

	Fields that are going to pass: product_name, product_price, product_quantity
	"""
	class Meta:
		model = Item
		fields = ('pk','product_id','product_name','product_price', 'product_quantity' )

class SaleDetailsSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model Sale.

	Fields that are going to pass: date, product, product_quantity, client,
	assistant, notes
	"""
	assistant = AssistantDetailsSerializer()
	client = ClientDetailsSerializer()
	transactions = serializers.SerializerMethodField()

	class Meta:
		model = Sale
		depth = 1
		fields = ('pk','date','item','client','assistant','notes','transactions')

	def get_transactions(self,obj):
		transactions = []
		print(Transaction.objects.filter(sale=obj))
		for transaction in Transaction.objects.filter(sale=obj):
			data = {}
			bank = {}
			pay_method = {}
			data['pk'] = transaction.pk
			data['date'] = transaction.date
			data['amount'] = transaction.amount
			if (transaction.pay_method):
				pay_method['pk'] = transaction.pay_method.pk
				pay_method['description'] = transaction.pay_method.description
			data['pay_method'] = pay_method
			if (transaction.bank):
				bank['pk'] = transaction.bank.pk
				bank['name'] = transaction.bank.name
			data['bank'] = bank
			data['reference_number'] = transaction.reference_number
			transactions.append(data)
		return transactions

class DebtSerializer(serializers.ModelSerializer):
	"""
			if (transaction.bank):
				bank['pk'] = transaction.bank.pk
				bank['name'] = transaction.bank.name
			data['bank'] = bank
			data['reference_number'] = transaction.reference_number
			transactions.append(data)
		return transactions

	"""

class DebtSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model Debt.

	Fields that are going to pass: date, assistant, product, product_quantity, status, debt_payment
	"""

	class Meta:
		model = Debt
		fields = ('pk','date','assistant','product','product_quantity','status','debt_payment')

class DebtPaymentSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model DebtPayment.

	Fields that are going to pass: date, assistant
	"""

	class Meta:
		model = DebtPayment
		fields = ('pk','date','assistant')


class DebtPaymentDetailsSerializer(serializers.ModelSerializer):
	"""
	Consist in the serializer of model DebtPayment.

	Fields that are going to pass: date, assistant
	"""

	transactions = serializers.SerializerMethodField()


	class Meta:
		model = DebtPayment
		fields = ('pk','date','assistant','transactions')

	def get_transactions(self,obj):
		transactions = []
		for transaction in Transaction.objects.filter(debt_payment=obj):
			data = {}
			bank = {}
			pay_method = {}
			data['pk'] = transaction.pk
			data['date'] = transaction.date
			data['amount'] = transaction.amount
			if (transaction.pay_method):
				pay_method['pk'] = transaction.pay_method.pk
				pay_method['description'] = transaction.pay_method.description
			data['pay_method'] = pay_method
			if (transaction.bank):
				bank['pk'] = transaction.bank.pk
				bank['name'] = transaction.bank.name
			data['bank'] = bank
			data['reference_number'] = transaction.reference_number
			transactions.append(data)
		return transactions
