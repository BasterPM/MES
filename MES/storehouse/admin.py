from django.contrib import admin
from .models import MethodObtaining, UnitMeasurement, Storehouse, FinalProduct, AssemblyUnit, OwnProduction

admin.site.register(MethodObtaining)
admin.site.register(UnitMeasurement)
admin.site.register(Storehouse)
admin.site.register(FinalProduct)
admin.site.register(AssemblyUnit)
admin.site.register(OwnProduction)
