from django import forms
from .models import Order, Bike, Accessories, Customer

class OrderForm(forms.ModelForm):
    bikes = forms.ModelMultipleChoiceField(
        queryset=Bike.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Bicicletas"
    )
    accessories = forms.ModelMultipleChoiceField(
        queryset=Accessories.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Accesorios"
    )
    bike_quantities = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )
    accessory_quantities = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )

    class Meta:
        model = Order
        fields = ['client', 'country', 'city', 'address', 'method_payment', 'bikes', 'accessories']

    def clean(self):
        cleaned_data = super().clean()
        bike_quantities = cleaned_data.get('bike_quantities')
        accessory_quantities = cleaned_data.get('accessory_quantities')
        # Convertir las cantidades a diccionarios
        cleaned_data['bike_quantities'] = self._parse_quantities(bike_quantities)
        cleaned_data['accessory_quantities'] = self._parse_quantities(accessory_quantities)
        return cleaned_data

    def _parse_quantities(self, quantities_str):
        quantities = {}
        if quantities_str:
            for item in quantities_str.split(','):
                pk, quantity = item.split(':')
                quantities[int(pk)] = int(quantity)
        return quantities
class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ['name', 'price', 'stock', 'description', 'categories', 'product_picture', 'brand_bikes']

class AccessoriesForm(forms.ModelForm):
    class Meta:
        model = Accessories
        fields = ['name', 'price', 'stock', 'description', 'categories', 'product_picture', 'product_category', 'brand_accesories']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'last_name', 'id_card', 'email', 'phone_number', 'genre', 'address']