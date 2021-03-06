from django.urls import path, re_path
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='MACAPI')

from . import views

urlpatterns = [
    url(r'^$', schema_view),
    path('taquilla-api/product/', views.ProductListCreate.as_view()),
    url(r'^taquilla-api/product/(?P<pk>\d+)/$',views.ProductRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/item/', views.ItemListCreate.as_view()),
    url(r'^taquilla-api/item/(?P<pk>\d+)/$',views.ItemRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/client/', views.ClientListCreate.as_view()),
    url(r'^taquilla-api/client/(?P<id_document>[-\w\d]+)/$',views.ClientRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/interest/', views.InterestListCreate.as_view()),
    url(r'^taquilla-api/interest/(?P<pk>\d+)/$',views.InterestRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/assistant/', views.AssistantListCreate.as_view()),
    url(r'^taquilla-api/assistant/(?P<id_document>[-\w\d]+)/$',views.AssistantRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/accounthistory/', views.AccountHistoryListCreate.as_view()),
    url(r'^taquilla-api/accounthistory/(?P<date>[-\w\d]+)/$',views.AccountHistoryRetrieveUpdateDestroy.as_view()),
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
    url(r'^taquilla-api/auth/obtain_token/', obtain_jwt_token),
    url(r'^taquilla-api/auth/refresh_token/', refresh_jwt_token),
    
]