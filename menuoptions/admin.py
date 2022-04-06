from django.contrib import admin
from .models import MenuOption, Category

# Register your models here.


class MenuOptionAdmin(admin.ModelAdmin):
    """ Customised admin to add fields """
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )


ordering = ('category', 'name')


class CategoryAdmin(admin.ModelAdmin):
    """ Customised admin to add fields """
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(MenuOption, MenuOptionAdmin)
admin.site.register(Category, CategoryAdmin)
