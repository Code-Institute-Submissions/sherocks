from django.contrib import admin
from .models import Company, Office, Employee


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'phone_number',
    )


class OfficeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'company',
    )


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'email',
        'phone_number',
        'office',
        'role',
        'image',
    )


admin.site.register(Company, CompanyAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(Employee, EmployeeAdmin)
