from django.contrib import admin

from .models import Employee, EmployeePosition

admin.site.register(Employee)
admin.site.register(EmployeePosition)
