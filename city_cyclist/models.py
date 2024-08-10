from django.db import models
from django.core.exceptions import ValidationError

class Category(models.Model):
    category_name = models.CharField(max_length=30, null=False, unique=True)

    def __str__(self):
        return self.category_name
    
class Brand(models.Model):
    brand_name = models.CharField(max_length=30, null=False, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.brand_name


class Bike(models.Model):
    model_name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    stock = models.PositiveIntegerField() 
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bike_picture = models.ImageField(upload_to='bike_images', blank=True, null=True)  
    
    def __str__(self):
        return f'{self.brand} {self.model_name}'


class Product(models.Model):
    product_name = models.CharField(max_length=30, unique=True)
    PRODUCT_CATEGORY= {
        ("Aros", "Aros"),
        ("Casco", "Casco"),
        ("Frenos", "Frenos"),
        ("Luces","Luces"),
        ("Pedales", "Pedales"),
        ("Rueda", "Rueda")
    }
    product_category = models.CharField(max_length=30, choices=PRODUCT_CATEGORY, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    description = models.TextField(blank=True, null=True)
    stock = models.PositiveIntegerField()
    product_picture = models.ImageField(upload_to='product_images', blank=True, null=True) 

    def __str__(self):
        return self.product_name


class Customer(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id_card = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50, )

    def id_card_verification(self):
        if len(self.id_card) != 10:
            raise ValidationError('El número de cédula debe tener exactamente 10 caracteres.')

    def __str__(self):
        return f'{self.name} {self.last_name}'


class PaymentType(models.Model):
    pay_name = models.CharField(max_length=30, null=False, unique=True)

    def __str__(self):
        return self.pay_name

class Shopping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    bike = models.ManyToManyField(Bike, blank=True)
    products = models.ManyToManyField(Product, blank=True) 
    total = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.RESTRICT)
    total = models.DecimalField(max_digits=10, decimal_places=2)
       
    def __str__(self):
        return f'Shopping {self.id} - Customer: {self.customer}'
