from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """ Customised admin to add fields """
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    """ Customised admin to add fields """
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
