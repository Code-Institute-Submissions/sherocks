from django.contrib import admin
from .models import Product, Category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'brand',
        'description',
        'has_sizes',
        'material',
        'price',
        'image',
        'sku',
    )
    ordering = ('brand',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
