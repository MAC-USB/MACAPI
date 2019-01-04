from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from datetime import datetime

class Product(models.Model):
	"""
	
	It consists of the table of products.

	Parameters:
	models.Model (Product): is the instance on which the table is created. (Articulos)

	Attributes of the class:
	Name: Name of the product.
	Price: Price of the product.
	"""
	name = models.CharField(max_length=50,validators=[RegexValidator(regex='^[a-zA-Záéíóúñ/ ]+$',message='Invalid name')])
	price = models.FloatField(default=0)

	def __str__(self):
    		return str(self.name)
	
class Client(models.Model):
	"""
	It consists of the table of clients.

	Parameters:
	models.Model (Client): is the instance on which the table is created. (Clientes)

	Attributes of the class:
	id_document: Client ID Document (Cedula)
	first_name: First name of the Client
	last_name: Last name of the Client
	"""
	id_document = models.CharField(primary_key=True, max_length=10,validators=[RegexValidator(regex="^[V|E|J|P]\-[0-9]{5,8}$",message="Invalid document id")])
	first_name = models.CharField(max_length=50,validators=[RegexValidator(regex="^[a-zA-Záéíóúñ]+$",message='Invalid first name')])
	last_name = models.CharField(max_length=50,validators=[RegexValidator(regex="^[a-zA-Záéíóúñ]+$",message='Invalid last name')])
	phone_number = models.CharField(max_length=15,validators=[RegexValidator(regex="[(]?\d{3}[)]?\s?-?\s?\d{3}\s?-?\s?\d{4}",message='Invalid Phone')])

	def __str__(self):
    		return str(self.id_document)
class Interest(models.Model):
	"""
	It consists of the table of interest.

	Parameters:
	models.Model (Interest): is the instance on which the table is created. (Intereses)

	Attributes of the class:
	percentage: Percentage of interest
	range_days: Range of days
	"""
	percentage = models.FloatField(default=0)
	range_days = models.IntegerField(default=0)

	def __str__(self):
    		return str(self.percentage)
class Assistant(models.Model):
	"""
    It consists of the table of assistants.

	Parameters:
	models.Model (Assistant): is the instance on which the table is created. (Preparador)

	Attributes of the class:
	id_document: Assistant ID Document (Cedula)
	first_name: First name of the Assistant
	last_name: Last name of the Assistant
	email: Email of the Assistant
	debt_amount: amount of debt accumulated by the assistant
	debt_date: Debt date by the assistant
	"""
	id_document = models.CharField(primary_key=True, max_length=10,validators=[RegexValidator(regex="^[V|E|J|P]\-[0-9]{5,8}$",message="Invalid id document")])
	initials = models.CharField(default=None,max_length=3,validators=[RegexValidator(regex='[A-Z]{2,3}',message='Invalid initials')])
	first_name = models.CharField(max_length=50,validators=[RegexValidator(regex='^[a-zA-Záéíóúñ]+$',message='Invalid first name')])
	last_name = models.CharField(max_length=50,validators=[RegexValidator(regex='^[a-zA-Záéíóúñ ]+$',message='Invalid last name')])
	email = models.EmailField(max_length=40,null=True,blank=True,validators=[RegexValidator(regex='([a-zA-Z0-9_-]+\.?){1,}@[a-z]+\.[a-z]{1,}', message='Invalid email')])
	debt_amount = models.FloatField(default=0)
	debt_date = models.DateTimeField(default=None,null=True)

	def __str__(self):
			return str(self.initials)

class AccountHistory(models.Model):
	"""
    It consists of the table of account history.

	Parameters:
	models.Model (AccountHistory): is the instance on which the table is created. (HistorialCuenta)

	Attributes of the class:
	date: Date of account history
	ideal_amount_cash: Amount of ideal cash (cant_ideal_efectivo)
	ideal_amount_account: Amount of ideal account (cant_ideal_caja)
	real_amount_cash: Amount of real cash (cant_real_efectivo)
	real_amount_account: Amount of real account (cant_real_caja)
	"""
	date = models.DateTimeField(primary_key=True)
	ideal_amount_cash = models.FloatField(default=0)
	ideal_amount_account = models.FloatField(default=0)
	real_amount_cash = models.FloatField(default=0)
	real_amount_account = models.FloatField(default=0)

	def __str__(self):
    		return str(self.date)

class PayMethod(models.Model):
	"""
	It consists of the table of Pay Methods.

	Parameters:
	models.Model (PaYMethod): is the instance on which the table is created.

	Attributes of the clayss:
	description: Description about how the transaction was maked
	"""
	description = models.CharField(max_length=30,validators=[RegexValidator(regex='^[a-zA-Záéíóúñ ]+$',message='Invalid description')])

class Bank(models.Model):
	"""
	It consists of the table of Banks.

	Parameters:
	models.Model (Bank): is the instance on which the table is created.

	Attributes of the class:
	pay_method: Pay method of Bank
	name: Name of bank
	code: Code of bank
	"""

	name = models.CharField(max_length=30,validators=[RegexValidator(regex='^[a-zA-Záéíóúñ ]+$',message='Invalid name')])
	code = models.IntegerField(validators=[MaxValueValidator(9999)],default=0)
	
	def __str__(self):
    		return str(self.name)


class Transaction(models.Model):
	"""
	It consists of the table of Transaction on Taquilla.

	Parameters:
	models.Model (Transaction): is the instance on which the table is created.

	Attributes of the class:
	date: Date of Transaction
	amount: Transaction amount
	types: Type of the transaction (In discussion)
	"""
	date = models.DateTimeField(default=datetime.now)
	amount = models.FloatField(default=None)
	types = models.CharField(max_length=30,null=True,validators=[RegexValidator(regex='^[a-zA-Záéíóúñ ]+$',message='Tipo invalido')])

	def __str__(self):
    		return str(self.date)

class Sale(models.Model):
	"""
	It's about a Transaction subclass, and consist in the sale on Taquilla

	Parameters:
	models.Model (Sale): is the instance on which the table is created.

	Attributes of the class:
	transaction: Transaction associated to the sale
	product_quantity: Quantity of product
	product: What product was sell
	pay_method: Method to pay the sale
	bank: If pay_method was a bank transfer, the bank
	client: What client buy the product
	assistant: What assistant sell the product
	notes: Notes about the sale
	"""
	transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
	product_quantity = models.IntegerField(default=0)
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	pay_method = models.ForeignKey(PayMethod, on_delete=models.CASCADE, default=None)
	bank = models.ForeignKey(Bank, on_delete=models.CASCADE, default=None)
	confirmation_no = models.IntegerField(default=None)
	client = models.ForeignKey(Client,on_delete=models.CASCADE)
	assistant = models.ForeignKey(Assistant,on_delete=models.CASCADE)
	notes = models.CharField(max_length=60,null=True)


class Debt(models.Model):
	"""
	It's about a Transaction subclass, and consist in the register debt by the assistants to acquire some product. (Deuda)

	Parameters:
		models.Model (Debt): is the instance on which the table is created.

	Attributes of the class:
		transaction : Reference to the Transaction table, the superclass.
		product : Reference to the requested product.
		product_quantity : Quantity of requested product.
		assistant : Reference to the assistant.
	"""
	transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	product_quantity = models.IntegerField(default=0)
	assistant = models.ForeignKey(Assistant,on_delete=models.CASCADE)

class DebtPayment(models.Model):
	"""
	It's about a Transaccion subclass, and consist in payment of acumulated debt by a assistant

	Parameters:
		models.Model (DebtPayment): is the instance on which the table is created.

	Attributes of the class:
		transaction : Reference to the transaction table, the superclass.
		debt_amount : Amount of paid debt.
		pay_method : Type of payment.
		bank : If payment made on bank transfer, the bank.
		confirmation_no : If payment made on bank transfer, the confirmation number.
		pay_date : Date of paid debt.
		assitant : Reference to the assistant.
	"""
	transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
	debt_amount = models.FloatField(default=0)
	pay_method = models.ForeignKey(PayMethod, on_delete=models.CASCADE)
	bank = models.ForeignKey(Bank, on_delete=models.CASCADE, default=None)
	confirmation_no = models.IntegerField(default=None)
	pay_date = models.DateTimeField(default=datetime.now)
	assistant = models.ForeignKey(Assistant,on_delete=models.CASCADE)
