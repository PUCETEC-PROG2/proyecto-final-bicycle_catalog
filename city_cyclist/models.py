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

class Bike(models.Model):
    bike_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, 
                                validators=[MinValueValidator(100.00, message="La Bicleta mas económica cuesta $100")]) 
    stock = models.PositiveIntegerField() 
    description = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(BrandBikes, on_delete=models.CASCADE) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bike_picture = models.ImageField(upload_to='bike_images', blank=True, null=True)

    
    def __str__(self):
        return f'{self.bike_name} - {self.brand} - {self.category}'


class Accessories(models.Model):
    name_accessories = models.CharField(max_length=30, unique=True)
    PRODUCT_CATEGORY= {
        ("Aros", "Aros"),
        ("Casco", "Casco"),
        ("Frenos", "Frenos"),
        ("Luces","Luces"),
        ("Pedales", "Pedales"),
        ("Rueda", "Rueda")
    }
    product_category = models.CharField(max_length=30, choices=PRODUCT_CATEGORY, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0.99, message="El producto mas económico cuesta 0,99")]) 
    stock = models.PositiveIntegerField() 
    description = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(BrandAccessories, on_delete=models.CASCADE) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_picture = models.ImageField(upload_to='product_images', blank=True, null=True)

    def __str__(self):
       return f'{self.name_accessories} - {self.brand} - {self.category}'


class Customer(models.Model):
    name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    id_card = models.CharField(unique=True,validators=[
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
    address = models.CharField(max_length=50, )

    def __str__(self):
        return f'{self.name} {self.last_name}'


class PaymentType(models.Model):
    pay_name = models.CharField(max_length=30, null=False, unique=True)

    def __str__(self):
        return self.pay_name
    

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    country = models.CharField(max_length=30, null=False)
    city = models.CharField(max_length=30, null=False)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.RESTRICT)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    paid = models.BooleanField(default=False)
       
    def __str__(self):
        return f'Compra {self.id} - Cliente: {self.customer}'
    
    def calculate_total(self):
        total = Decimal('0.00')
        for item in self.shoppingitem_set.all():
            total += item.subtotal()
        self.total = total
        self.save()
        return self.total


class CartItem(models.Model):
    shopping = models.ForeignKey(Cart, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, blank=True, null=True)
    accessories = models.ForeignKey(Accessories, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        if self.bike:
            return self.quantity * self.bike.price
        elif self.accessories:
            return self.quantity * self.accessories.price
        return Decimal('0.00')

    def __str__(self):
        item_name = self.bike.model_name if self.bike else self.accessories.price
        item_price = self.bike.price if self.bike else self.accessories.price
        return f'{item_name} - Cantidad: {self.quantity} - Precio unitario: {item_price} - Subtotal: {self.subtotal()}'