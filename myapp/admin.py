from django.contrib import admin, messages

# Register your models here.
from django.contrib import admin
from django.db.models import F

from .models import Product, Category, Client, Order

'''
An F() object represents the value of a model field, transformed value of a model field, or annotated column. 
It makes it possible to refer to model field values and perform database operations using them without actually 
having to pull them out of the database into Python memory
'''


def add_stock(modeladmin, request, queryset):
    for product in queryset:
        if 0 <= product.stock +50 <= 1000:
            queryset.update(stock=F('stock') + 50)
        else:
            messages.error(request, "stock cannot more than 1000")


add_stock.short_description = 'Add 50 stocks'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'available')
    actions = [add_stock]


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'city', 'get_interested')


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order)
