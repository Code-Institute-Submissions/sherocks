from django.db import models


class Company(models.Model):
    class Meta:
        verbose_name_plural = "Companies"

    name = models.CharField(max_length=60, null=False, blank=False)
    address = models.CharField(max_length=60, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name


class Office(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE, related_name="office")

    def __str__(self):
        return self.name


class Employee(models.Model):
    full_name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    office = models.ForeignKey(
        'Office', on_delete=models.CASCADE, related_name="employee_in_office")
    role = models.CharField(max_length=30, null=False, blank=False)
    image = models.ImageField(upload_to='team', null=True, blank=True)

    def __str__(self):
        return f'{self.full_name}, {self.role} at {self.office}'
