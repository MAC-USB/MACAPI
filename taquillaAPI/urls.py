from django.urls import path, re_path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('taquilla-api/articulo/', views.ArticuloListCreate.as_view()),
    url(r'^taquilla-api/articulo/(?P<pk>\d+)/$',views.ArticuloRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/cliente/', views.ClienteListCreate.as_view()),
    url(r'^taquilla-api/cliente/(?P<cedula>[-\w\d]+)/$',views.ClienteRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/interes/', views.InteresListCreate.as_view()),
    url(r'^taquilla-api/interes/(?P<pk>\d+)/$',views.InteresRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/preparador/', views.PreparadorListCreate.as_view()),
    url(r'^taquilla-api/preparador/(?P<cedula>[-\w\d]+)/$',views.PreparadorRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/historialcuenta/', views.HistorialCuentaListCreate.as_view()),
    url(r'^taquilla-api/historialcuenta/(?P<fecha>[-\w\d]+)/$',views.HistorialCuentaRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/plataformapago/', views.PlataformaPagoListCreate.as_view()),
    url(r'^taquilla-api/plataformapago/(?P<pk>\d+)/$',views.InteresRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/transaccion/', views.TransaccionListCreate.as_view()),
    url(r'^taquilla-api/transaccion/(?P<pk>\d+)/$',views.TransaccionRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/venta/', views.VentaListCreate.as_view()),
    url(r'^taquilla-api/venta/(?P<pk>\d+)/$',views.VentaRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/deuda/', views.DeudaListCreate.as_view()),
    url(r'^taquilla-api/deuda/(?P<pk>\d+)/$',views.DeudaRetrieveUpdateDestroy.as_view()),
    path('taquilla-api/pagodeuda/', views.PagoDeudaListCreate.as_view()),
    url(r'^taquilla-api/pagodeuda/(?P<pk>\d+)/$',views.PagoDeudaRetrieveUpdateDestroy.as_view()),
    
]