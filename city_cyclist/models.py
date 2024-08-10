from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class Category(models.Model):
    category_name = models.CharField(max_length=30, null=False, unique=True)

    def __str__(self):
        return self.category_name
    
class Brand(models.Model):
    brand_name = models.CharField(max_length=30, null=False, unique=True)
    
    def __str__(self):
        return self.brand_name


class Bike(models.Model):
    model_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, 
                                validators=[MinValueValidator(100.00, message="La Bicleta mas económica cuesta $100")]) 
    stock = models.PositiveIntegerField() 
    description = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bike_picture = models.ImageField(upload_to='bike_images', blank=True, null=True)

    
    def __str__(self):
        return f'{self.model_name} - {self.brand} - {self.category}'


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
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0.99, message="El producto mas económico cuesta 0,99")]) 
    stock = models.PositiveIntegerField() 
    description = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_picture = models.ImageField(upload_to='product_images', blank=True, null=True)

    def __str__(self):
       return f'{self.product_name} - {self.brand} - {self.category}'


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
    

class Shopping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    country = models.CharField(max_length=30, null=False)
    city = models.CharField(max_length=30, null=False)
    bike = models.ManyToManyField(Bike, blank=True)
    products = models.ManyToManyField(Product, blank=True) 
    payment_type = models.ForeignKey(PaymentType, on_delete=models.RESTRICT)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
       
    def __str__(self):
        return f'Shopping {self.id} - Customer: {self.customer}'
    

    def calculate_total(self):
        total_bikes = self.bike.aggregate(total=models.Sum('price'))['total'] or 0
        total_products = self.products.aggregate(total=models.Sum('price'))['total'] or 0
        return total_bikes + total_products
