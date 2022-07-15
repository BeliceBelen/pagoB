from django.contrib import admin
from .models import  Cliente, DetallePago, Pago, Servicio
from .models import Cobro, FichaInscripcion
# Register your models he
admin.site.register(Cliente)
admin.site.register(Cobro)
admin.site.register(Servicio)
admin.site.register(FichaInscripcion)
admin.site.register(Pago)
admin.site.register(DetallePago)

