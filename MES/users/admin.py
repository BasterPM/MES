from django.contrib import admin

from users.models import Employee, EmployeePosition, Role

admin.site.register(Employee)
admin.site.register(EmployeePosition)
admin.site.register(Role)
