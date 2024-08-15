from django import forms
from .models import Order, Bike, Accessories

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'country', 'city', 'address', 'method_payment']

class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ['name', 'price', 'stock', 'description', 'categories', 'product_picture', 'brand_bikes']

class AccessoriesForm(forms.ModelForm):
    class Meta:
        model = Accessories
        fields = ['name', 'price', 'stock', 'description', 'categories', 'product_picture', 'product_category', 'brand_accesories']