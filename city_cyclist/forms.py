from django import forms
from .models import Category, BrandBikes, BrandAccessories, Bike, Accessories, Customer, PaymentType, CartItem

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BrandBikesForm(forms.ModelForm):
    class Meta:
        model = BrandBikes
        fields = '__all__'
        widgets = {
            'brand_bike': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BrandAccessoriesForm(forms.ModelForm):
    class Meta:
        model = BrandAccessories
        fields = '__all__'
        widgets = {
            'brand_product': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'product_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'brand_bikes': forms.Select(attrs={'class': 'form-control'}),
        }

class AccessoriesForm(forms.ModelForm):
    class Meta:
        model = Accessories
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'product_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'product_category': forms.Select(attrs={'class': 'form-control'}),
            'brand_accesories': forms.Select(attrs={'class': 'form-control'}),
        }

     

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'id_card': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
        }
       

class PaymentTypeForm(forms.ModelForm):
    class Meta:
        model = PaymentType
        fields = '__all__'
        widgets = {
            'pay_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['customer', 'date', 'country', 'city', 'payment_type', 'bike', 'bicycle_numbers', 'accessories', 'accessorie_numbers']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_type': forms.Select(attrs={'class': 'form-control'}),
            'bike': forms.Select(attrs={'class': 'form-control'}),
            'bicycle_numbers': forms.NumberInput(attrs={'class': 'form-control'}),
            'accessories': forms.Select(attrs={'class': 'form-control'}),
            'accessorie_numbers': forms.NumberInput(attrs={'class': 'form-control'}),
        }
