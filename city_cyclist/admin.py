from django.contrib import admin
from .models import Category, Bike, Accessories, Customer, PaymentType, BrandBikes, CartItem, BrandAccessories


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    pass

@admin.register(Accessories)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    pass
        

@admin.register(BrandBikes)
class BrandBikesAdmin(admin.ModelAdmin):
    pass

@admin.register(BrandAccessories)
class BrandProductsAdmin(admin.ModelAdmin):
    pass

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass