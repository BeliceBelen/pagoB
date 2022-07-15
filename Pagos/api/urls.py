from django.urls import path
#from . import views
from .views import ClienteView, CobroView,ServicioView, PagoView
from .views import FichaInscripcionView,DetallePagoView
#urlpatterns = [
#    path('', views.inicio,name='index'),
#]

urlpatterns = [
    path('clientes/', ClienteView.as_view(),name='clientes_list'),
    path('clientes/<int:id>', ClienteView.as_view(),name='clientes_process'),
    path('cobros/', CobroView.as_view(),name='cobros_list'),
    path('cobros/<int:id>', CobroView.as_view(),name='cobros_process'),
    path('servicios/', ServicioView.as_view(),name='servicios_list'),
    path('servicios/<int:id>', ServicioView.as_view(),name='servicios_process'),
    path('inscripciones/', FichaInscripcionView.as_view(),name='inscripciones_list'),
    path('inscripciones/<int:id>', FichaInscripcionView.as_view(),name='inscripciones_process'),
    path('pagos/', PagoView.as_view(),name='pagos_list'),
    path('pagos/<int:id>', PagoView.as_view(),name='pagos_process'),
    path('detalles/', DetallePagoView.as_view(),name='detalles_list'),
    path('detalles/<int:id>', DetallePagoView.as_view(),name='detalles_process'),
]