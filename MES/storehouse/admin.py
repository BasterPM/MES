from django.contrib import admin
from .models import MethodObtaining, UnitMeasurement, Storehouse, FinalProduct, AssemblyUnit, OwnProduction,\
    TechnologicalProcess, Seller

admin.site.register(MethodObtaining)
admin.site.register(UnitMeasurement)
admin.site.register(Storehouse)
admin.site.register(FinalProduct)
admin.site.register(AssemblyUnit)
admin.site.register(OwnProduction)
admin.site.register(TechnologicalProcess)
admin.site.register(Seller)
