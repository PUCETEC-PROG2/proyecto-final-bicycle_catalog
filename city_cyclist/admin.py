from django.contrib import admin
from .models import Category, Bike, Product, Customer, PaymentType, Shopping, Brand, ShoppingItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Shopping)
class ShoppingAdmin(admin.ModelAdmin):
    def no_delete(self, request, obj=None):
        return False         

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(ShoppingItem)
class ShoppingItemAdmin(admin.ModelAdmin):
    pass