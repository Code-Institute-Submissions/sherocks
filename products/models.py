from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    friendly_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, blank=True)
    name = models.CharField(max_length=160)
    brand = models.CharField(max_length=100)
    description = models.TextField()
    material = models.CharField(max_length=160)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024)
    image = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.name

