from django.urls import path, re_path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('taquilla-api/product/', views.ProductListCreate.as_view()),
    url(r'^taquilla-api/product/(?P<pk>\d+)/$',views.ProductRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/client/', views.ClientListCreate.as_view()),
    url(r'^taquilla-api/client/(?P<cedula>[-\w\d]+)/$',views.ClientRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/interest/', views.InterestListCreate.as_view()),
    url(r'^taquilla-api/interest/(?P<pk>\d+)/$',views.InterestRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/assistant/', views.AssistantListCreate.as_view()),
    url(r'^taquilla-api/assistant/(?P<cedula>[-\w\d]+)/$',views.AssistantRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/accounthistory/', views.AccountHistoryListCreate.as_view()),
    url(r'^taquilla-api/accounthistory/(?P<fecha>[-\w\d]+)/$',views.AccountHistoryRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/bank/', views.BankListCreate.as_view()),
    url(r'^taquilla-api/bank/(?P<pk>\d+)/$',views.BankRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/paymethod/', views.PayMethodListCreate.as_view()),
    url(r'^taquilla-api/paymethod/(?P<pk>\d+)/$',views.PayMethodRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/transaction/', views.TransactionListCreate.as_view()),
    url(r'^taquilla-api/transaction/(?P<pk>\d+)/$',views.TransactionRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/sale/', views.SaleListCreate.as_view()),
    url(r'^taquilla-api/sale/(?P<pk>\d+)/$',views.SaleRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/debt/', views.DebtListCreate.as_view()),
    url(r'^taquilla-api/debt/(?P<pk>\d+)/$',views.DebtRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/debtpayment/', views.DebtPaymentListCreate.as_view()),
    url(r'^taquilla-api/debtpayment/(?P<pk>\d+)/$',views.DebtPaymentRetrieveUpdateDestroy.as_view()),
    
]