from django.contrib import admin
from .models import Category, Bike, Product, Customer, PaymentType, Cart, BrandBikes, CartItem, BrandProducts


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

@admin.register(Cart)
class ShoppingAdmin(admin.ModelAdmin):
    def no_delete(self, request, obj=None):
        return False         

@admin.register(BrandBikes)
class BrandBikesAdmin(admin.ModelAdmin):
    pass

@admin.register(BrandProducts)
class BrandProductsAdmin(admin.ModelAdmin):
    pass

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass