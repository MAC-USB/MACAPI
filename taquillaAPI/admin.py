from django.contrib import admin
from .models import *

# Register your models here.

from django.contrib import admin

#Settings of Product on Admin page

class ProductAdmin(admin.ModelAdmin):

    fieldsets = [
        ('name', {'fields': ['name']}),
        ('price', {'fields': ['price']}),
    ]
    list_display = ('name', 'price')
    list_filter = ['name','price']

admin.site.register(Product, ProductAdmin)

#Settings of Item on Admin page

class ItemAdmin(admin.ModelAdmin):

    fieldsets = [
        ('product_id', {'fields': ['product_id']}),
        ('product_name', {'fields': ['product_name']}),
        ('product_price', {'fields': ['product_price']}),
        ('product_quantity', {'fields': ['product_quantity']}),


    ]
    list_display = ('product_id', 'product_name','product_price','product_quantity')
    list_filter = ['product_id', 'product_name','product_price','product_quantity']

admin.site.register(Item, ItemAdmin)

#Settings of Client on Admin page

class ClientAdmin(admin.ModelAdmin):

    fieldsets = [
        ('id_document', {'fields': ['id_document']}),
        ('first_name', {'fields': ['first_name']}),
        ('last_name', {'fields': ['last_name']}),
        ('phone_number', {'fields': ['phone_number']}),


    ]
    list_display = ('id_document','first_name','last_name','phone_number')
    list_filter = ['id_document','first_name','last_name','phone_number']

admin.site.register(Client, ClientAdmin)

#Settings of Interest on Admin page

class InterestAdmin(admin.ModelAdmin):

    fieldsets = [
        ('percentage', {'fields': ['percentage']}),
        ('range_days', {'fields': ['range_days']}),

    ]
    list_display = ('percentage','range_days')
    list_filter = ['percentage','range_days']

admin.site.register(Interest, InterestAdmin)

#Settings of Assistant on Admin page

class AssistantAdmin(admin.ModelAdmin):

    fieldsets = [
        ('id_document', {'fields': ['id_document']}),
        ('initials', {'fields': ['initials']}),
        ('first_name', {'fields': ['first_name']}),
        ('last_name', {'fields': ['last_name']}),
        ('email', {'fields': ['email']}),
        ('debt_amount', {'fields': ['debt_amount']}),
        ('debt_date', {'fields': ['debt_date']}),

    ]
    list_display = ('id_document','initials','first_name','last_name','email','debt_amount','debt_date')
    list_filter = ['id_document','initials','first_name','last_name','email','debt_amount','debt_date']

admin.site.register(Assistant, AssistantAdmin)

#Settings of Account History on Admin page

class AccountHistoryAdmin(admin.ModelAdmin):

    fieldsets = [
        ('date', {'fields': ['date']}),
        ('ideal_amount_cash', {'fields': ['ideal_amount_cash']}),
        ('ideal_amount_account', {'fields': ['ideal_amount_account']}),
        ('real_amount_cash', {'fields': ['real_amount_cash']}),
        ('real_amount_account', {'fields': ['real_amount_account']}),
    ]
    list_display = ('date','ideal_amount_cash','ideal_amount_account','real_amount_cash','real_amount_account')
    list_filter = ['date','ideal_amount_cash','ideal_amount_account','real_amount_cash','real_amount_account']

admin.site.register(AccountHistory, AccountHistoryAdmin)

#Settings of PayMethod on Admin page

class PayMethodAdmin(admin.ModelAdmin):

    fieldsets = [
        ('description', {'fields': ['description']}),

    ]
    list_display = ('description',)
    list_filter = ['description']

admin.site.register(PayMethod, PayMethodAdmin)

#Settings of Bank on Admin page

class BankAdmin(admin.ModelAdmin):

    fieldsets = [
        ('name', {'fields': ['name']}),
        ('code', {'fields': ['code']}),

    ]
    list_display = ('name','code')
    list_filter = ['name','code']

admin.site.register(Bank, BankAdmin)

#Settings of Sale on Admin page

class SaleAdmin(admin.ModelAdmin):

    fieldsets = [
        ('date', {'fields': ['date']}),
        ('item', {'fields': ['item']}),
        ('client', {'fields': ['client']}),
        ('assistant', {'fields': ['assistant']}),
        ('notes', {'fields': ['notes']}),
    ]
    list_display = ('date','client','assistant','notes')
    list_filter = ['date','item','client','assistant','notes']

admin.site.register(Sale, SaleAdmin)

#Settings of Debt Payment on Admin pages

class DebtPaymentAdmin(admin.ModelAdmin):

    fieldsets = [
        ('date', {'fields': ['date']}),
        ('assistant', {'fields': ['assistant']}),

    ]
    list_display = ('date','assistant')
    list_filter = ['date','assistant']

admin.site.register(DebtPayment, DebtPaymentAdmin)

#Settings of Debt on Admin pages

class DebtAdmin(admin.ModelAdmin):

    fieldsets = [
        ('date', {'fields': ['date']}),
        ('assistant', {'fields': ['assistant']}),
        ('item', {'fields': ['item']}),
        ('status', {'fields': ['status']}),
        ('debt_payment', {'fields': ['debt_payment']}),

    ]
    list_display = ('date','assistant','item','status','debt_payment')
    list_filter = ['date','assistant','item','status','debt_payment']

admin.site.register(Debt, DebtAdmin)

#Settings of Transaction on Admin pages

class TransactionAdmin(admin.ModelAdmin):

    fieldsets = [
        ('date', {'fields': ['date']}),
        ('amount', {'fields': ['amount']}),
        ('pay_method', {'fields': ['pay_method']}),
        ('bank', {'fields': ['bank']}),
        ('reference_number', {'fields': ['reference_number']}),
        ('sale', {'fields': ['sale']}),
        ('debt_payment', {'fields': ['debt_payment']}),



    ]
    list_display = ('date','amount','pay_method','bank','pay_method','reference_number','sale','debt_payment')
    list_filter = ['date','amount','pay_method','bank','pay_method','reference_number','sale','debt_payment']

admin.site.register(Transaction, TransactionAdmin)