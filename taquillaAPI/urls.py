from django.urls import path, re_path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('taquilla-api/articulo/', views.ArticuloList.as_view()),
    url(r'^taquilla-api/articulo/(?P<pk>\d+)/edit$',views.ArticuloUpdate.as_view()),
    url(r'^taquilla-api/articulo/(?P<pk>\d+)/delete$',views.ArticuloDestroy.as_view()),
    path('taquilla-api/cliente/', views.ClienteList.as_view()),
    path('taquilla-api/interes/', views.InteresList.as_view()),
    path('taquilla-api/preparador/', views.PreparadorList.as_view()),
    path('taquilla-api/historialcuenta/', views.HistorialCuentaList.as_view()),
    path('taquilla-api/plataformapago/', views.PlataformaPagoList.as_view()),
    path('taquilla-api/transaccion/', views.TransaccionList.as_view()),
    path('taquilla-api/venta/', views.VentaList.as_view()),
    path('taquilla-api/deuda/', views.DeudaList.as_view()),
    path('taquilla-api/pagodeuda/', views.PagoDeudaList.as_view()),
]