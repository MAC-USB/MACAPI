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

class Item(models.Model):
	"""

	It consists of the table of products.

	Parameters:
	models.Model (Product): is the instance on which the table is created. (Articulos)

	Attributes of the class:
	Name: Name of the product.
	Price: Price of the product.
	"""
	product_id = models.IntegerField()
	product_name = models.CharField(max_length=50,validators=[RegexValidator(regex='^[a-zA-Záéíóúñ/ ]+$',message='Invalid name')])
	product_price = models.FloatField(default=0)
	product_quantity = models.IntegerField(default=0)

	def __str__(self):
    		return str(self.product_name)

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
	models.Model (PaYMethod): is the instance on which the table is created. (MetodoPago)

	Attributes of the clayss:
	description: Description about how the transaction was maked
	"""
	description = models.CharField(max_length=30,validators=[RegexValidator(regex='^[a-zA-Záéíóúñ ]+$',message='Invalid description')])

	def __str__(self):
    		return str(self.description)


class Bank(models.Model):
	"""
	It consists of the table of Banks.

	Parameters:
	models.Model (Bank): is the instance on which the table is created. (Banco)

	Attributes of the class:
	pay_method: Pay method of Bank
	name: Name of bank
	code: Code of bank
	"""

	name = models.CharField(max_length=30,validators=[RegexValidator(regex='^[a-zA-Záéíóúñ ]+$',message='Invalid name')])
	code = models.IntegerField(validators=[MaxValueValidator(9999)],default=0)

	def __str__(self):
    		return str(self.name)



class Sale(models.Model):
	"""
	It's about a Transaction subclass, and consist in the sale on Taquilla

	Parameters:
	models.Model (Sale): is the instance on which the table is created. (Venta)

	Attributes of the class:
	date: Sale date.
	item: What product was sell, refered on item
	client: What client buy the product
	assistant: What assistant sell the product
	notes: Notes about the sale
	"""
	date = models.DateTimeField(default=datetime.now)
	item = models.ManyToManyField(Item)
	client = models.ForeignKey(Client,on_delete=models.CASCADE)
	assistant = models.ForeignKey(Assistant,on_delete=models.CASCADE)
	notes = models.CharField(max_length=60,blank=True)

	def __str__(self):
    		return str(self.date)



class DebtPayment(models.Model):
	"""
	It's about a Transaccion subclass, and consist in payment of acumulated debt by a assistant

	Parameters:
		models.Model (DebtPayment): is the instance on which the table is created. (PagoDeuda)

	Attributes of the class:
		pay_date : Date of paid debt.
		assistant : Reference to the assistant.
	"""
	date = models.DateTimeField(default=datetime.now)
	assistant = models.ForeignKey(Assistant,on_delete=models.CASCADE)

	def __str__(self):
    		return str(self.date)

class Debt(models.Model):
	"""
	It consists of the table of Banks. Now it's stand alone.

	Parameters:
		models.Model (Debt): is the instance on which the table is created. (Deuda)

	Attributes of the class:
		date: Date of debt.
		assistant: What assistant debt the product.
		item : Reference to the requested product (item).
		status: If a debt is pending, processing or approved.
		debt_payment: If a debt is paid, the paid associated to this debt.

	"""

	PENDING = 1
	PROCESSING = 2
	APPROVED = 3
	STATUS_CHOICES = (
		(PENDING, 'pending'),
		(PROCESSING, 'processing'),
		(APPROVED, 'approved'),
	)
	date = models.DateTimeField(default=datetime.now)
	assistant = models.ForeignKey(Assistant,on_delete=models.CASCADE)
	item = models.ForeignKey(Item,on_delete=models.CASCADE)
	status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)
	debt_payment = models.ForeignKey(DebtPayment, on_delete=models.CASCADE ,null=True)

	def __str__(self):
    		return str(self.date)

class Transaction(models.Model):
	"""
	It consists of the table of Transaction on Taquilla.

	Parameters:
	models.Model (Transaction): is the instance on which the table is created.  (Transaccion)

	Attributes of the class:
	date: Date of Transaction
	amount: Transaction amount
	pay_method: Method to pay the transaction
	bank: If pay_method was a bank transfer, the bank. Optional
	reference_number : If payment made on bank transfer, the confirmation number.
	sale: If the transaction is associated with a sale, this sale. Optional.
	debt_payment: If the transaction is associated with a debt payment, this debt payment. Optional.


	"""
	date = models.DateTimeField(default=datetime.now)
	amount = models.FloatField()
	pay_method = models.ForeignKey(PayMethod, on_delete=models.CASCADE)
	bank = models.ForeignKey(Bank, on_delete=models.CASCADE,null=True)
	reference_number = models.IntegerField(default=0)
	sale = models.ForeignKey(Sale, on_delete=models.CASCADE, null=True)
	debt_payment = models.ForeignKey(DebtPayment, on_delete=models.CASCADE, null=True)



	def __str__(self):
    		return str(self.date)
