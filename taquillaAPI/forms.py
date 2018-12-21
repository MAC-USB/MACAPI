from django import forms
from django.forms import ModelForm
from .models import *
from django.core.exceptions import NON_FIELD_ERRORS

""" 
In the present file the forms of all the tables in the database 
for this application are presented.
"""

class ProductForm(ModelForm):
    """ Form to add an instance to the table of products.
    """
    class Meta:
        model = Product
        fields = ["name", "price"]

class ClientForm(ModelForm):
    """ Form to add an instance to the table of clients.
    """
    class Meta:
        model = Client
        fields = ["id_document","first_name", "last_name","phone_number"]

class InterestForm(ModelForm):
    """ Form to add an instance to the table of interest.
    """
    class Meta:
        model = Interest
        fields = ["percentage","range_days"]

class AssistantForm(ModelForm):
    """ Form to add an instance to the table of assistants.
    """
    class Meta:
        model = Assistant
        fields = ["id_document","initials","first_name", "last_name","debt_amount","debt_date"]

class AccountHistoryForm(ModelForm):
    """ Form to add an instance to the table of Account History.
    """
    class Meta:
        model = AccountHistory
        fields = ["date", "ideal_amount_cash","ideal_amount_account","real_amount_cash","real_amount_account"]

class PayMethodForm(ModelForm):
    """ Form to add an instance to the table of Pay Methods.
    """
    class Meta:
        model = PayMethod
        fields = ["description"]

class BankForm(ModelForm):
    """ Form to add an instance to the table of Banks.
    """
    class Meta:
        model = Bank
        fields = ["name"]

class TransactionForm(ModelForm):
    """ Form to add an instance to the table of Transaction.
    """
    class Meta:
        model = Transaction
        fields = ["date","amount"]

class SaleForm(ModelForm):
    """ Form to add an instance to the table of Sale, subclass of Transaction.
    """
    class Meta:
        model = Sale
        fields = ["transaction",
                "product_quantity",
                "product",
                "bank",
                "pay_method"
                "confirmation_no",
                "client",
                "assistant"
                ]

class DebtForm(ModelForm):
    """ Form to add an instance to the table of Debts, subclass of Transaction.
    """
    class Meta:
        model = Debt
        fields = ["transaction",
                "product",
                "product_quantity",
                "assistant"
                ]

class DebtPaymentForm(ModelForm):
    """ Form to add an instance to the table of Debt Payment, subclass of
    Transaction.
    """
    class Meta:
        model = DebtPayment
        fields = ["transaction",
                "debt_amount",
                "bank",
                "pay_method"
                "confirmation_no",
                "pay_date",
                "assistant",
                ]