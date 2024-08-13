from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from decimal import Decimal

class Category(models.Model):
    category_name = models.CharField(max_length=30, null=False, unique=True)

    def __str__(self):
        return self.category_name
    
class BrandBikes(models.Model):
    brand_bike = models.CharField(max_length=30, null=False, unique=True)
    
    def __str__(self):
        return self.brand_bike

class BrandAccessories(models.Model):
    brand_product = models.CharField(max_length=30, null=False, unique=True)
    
    def __str__(self):
        return self.brand_product

from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0.99, message="El producto más económico cuesta 0,99")])
    stock = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField('Category')
    product_picture = models.ImageField(upload_to='product_images', blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        categories = ", ".join([str(category) for category in self.categories.all()])
        return f'{self.name} - {categories}'

class Bike(Product):
    brand_bikes = models.ForeignKey('BrandBikes', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.brand_bikes} - Precio: {self.price} - Stock: {self.stock}'

class Accessories(Product):
    PRODUCT_CATEGORY = [
        ("Aros", "Aros"),
        ("Casco", "Casco"),
        ("Frenos", "Frenos"),
        ("Luces", "Luces"),
        ("Pedales", "Pedales"),
        ("Rueda", "Rueda")
    ]
    product_category = models.CharField(max_length=30, choices=PRODUCT_CATEGORY, null=False)
    brand_accesories = models.ForeignKey('BrandAccessories', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.brand_accesories} - Precio: {self.price} - Stock: {self.stock}'


class Customer(models.Model):
    name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    id_card = models.CharField(unique=True, validators=[
                                        RegexValidator(
                                            regex=r'^\d{10}$',
                                            message='El número de cédula debe tener 10 dígitos.'
                                        )
                                    ])
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(validators=[
                                        RegexValidator(
                                            regex=r'^\d{7,15}$',
                                            message='El número de teléfono debe tener entre 7 y 15 dígitos.'
                                        )
                                    ])
    GENRES = [
        ("Bigénero", "Bigénero"),
        ("Femenino", "Femenino"),
        ("Masculino", "Masculino"),
        ("No binario", "No binario"),
   ]
    genre = models.CharField(max_length=30, choices=GENRES, null=False)
    address = models.CharField(max_length=50, )

    def __str__(self):
        return f'{self.name} {self.last_name}'

class PaymentType(models.Model):
    pay_name = models.CharField(max_length=30, null=False, unique=True)

    def __str__(self):
        return self.pay_name
    
class CartItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    country = models.CharField(max_length=30, null=False)
    city = models.CharField(max_length=30, null=False)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.RESTRICT)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, blank=True, null=True)
    bicycle_numbers = models.PositiveIntegerField(default=1)
    accessories = models.ForeignKey(Accessories, on_delete=models.CASCADE, blank=True, null=True)
    accessorie_numbers = models.PositiveIntegerField(default=1)

    def subtotal(self):
        total = Decimal('0.00')
        
        if self.bike:
            total += self.bicycle_numbers * self.bike.price
        
        if self.accessories:
            total += self.accessorie_numbers * self.accessories.price
        
        return total

    def __str__(self):
        details = []

        if self.bike:
            details.append(
                f'Bicicleta: {self.bike.name} - Cantidad: {self.bicycle_numbers} - Precio unitario: {self.bike.price}'
            )
        
        if self.accessories:
            details.append(
                f'Accesorio: {self.accessories.name} - Cantidad: {self.accessorie_numbers} - Precio unitario: {self.accessories.price}'
            )

        if not details:
            details.append('Unknown Item')

        customer_name = self.customer.name if self.customer else 'Unknown Customer'
        customer_lastname = self.customer.last_name if self.customer else 'Unknown Lastname'

        details_str = ' | '.join(details)
        return f'{customer_name} {customer_lastname} - {details_str} - Subtotal: {self.subtotal()}'
