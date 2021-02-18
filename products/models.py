from django.db import models

from profiles.models import UserProfile


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

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
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    material = models.CharField(max_length=160)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='products', blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="reviewer")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviewed_item")
    review = models.CharField(max_length=160)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.user} for {self.product}'
