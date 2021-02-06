from django.contrib import admin
from .models import Product, Category, Review


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


class ReviewAdmin(admin.ModelAdmin):

    readonly_fields = (
        'created',
    )
    list_display = (
        'user',
        'product',
        'review',
        'created',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
