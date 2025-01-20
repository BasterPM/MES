from django.contrib import admin

from .models import Employee, EmployeePosition, Role

admin.site.register(Employee)
admin.site.register(EmployeePosition)
admin.site.register(Role)
