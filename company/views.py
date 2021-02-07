from django.shortcuts import render
from .models import Office, Employee


def view_company(request):
    template = "company/company.html"
    departments = Office.objects.all()
    employees = Employee.objects.all()
    context = {
        "departments": departments,
        "employees": employees,
    }
    return render(request, template, context)
