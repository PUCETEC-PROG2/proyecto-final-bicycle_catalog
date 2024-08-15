from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, RegexValidator

class Category(models.Model):
    """
    Representación de categoría. 
    Relacionada con productos en general
    """
    category_name = models.CharField(max_length=30, null=False, unique=True)

    def __str__(self) -> str:
        return f'{self.category_name}'

class BrandBikes(models.Model):
    """
    Representación de marca de bicicletas.  
    """
    brand_bike = models.CharField(max_length=30, null=False, unique=True)

    def __str__(self) -> str:
        return f'{self.brand_bike}'

class BrandAccessories(models.Model):
    """
    Representación de categoría. 
    Relacionada con productos en general
    """
    brand_product = models.CharField(max_length=30, null=False, unique=True)

    def __str__(self) -> str:
        return f'{self.brand_product}'

class Product(models.Model):
    """
    Clase padre de la que se desprenden accesorios y bicicletas
    """
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.99, message="El producto más económico cuesta 0,99")])
    stock = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField('Category')
    product_picture = models.ImageField(upload_to='product_images', blank=True, null=True)

    def __str__(self) -> str:
        categories = ", ".join([str(category) for category in self.categories.all()])
        return f'{self.name} - {categories}'
    class Meta:
        abstract = True

class Bike(Product):
    """
    Subclase de productos
    """
    brand_bikes = models.ForeignKey('BrandBikes', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} - {self.brand_bikes} - Precio: {self.price} - Stock: {self.stock}'

class Accessories(Product):
    """
    Subclase de productos
    """
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

    def __str__(self) -> str:
        return f'{self.name} - {self.brand_accesories} - Precio: {self.price} - Stock: {self.stock}'

class Customer(models.Model):
    """
    Clase que gestiona el objeto cliente / customer
    """
    name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    id_card = models.CharField(max_length=10, unique=True, validators=[
        RegexValidator(regex=r'^\d{10}$', message='El número de cédula debe tener 10 dígitos.')
    ])
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15, validators=[
       RegexValidator(regex=r'^\d{7,15}$', message='El número de teléfono debe tener entre 7 y 15 dígitos.')
    ])
    GENRES = [
        ("Bigénero", "Bigénero"),
        ("Femenino", "Femenino"),
        ("Masculino", "Masculino"),
        ("No binario", "No binario"),
    ]
    genre = models.CharField(max_length=30, choices=GENRES, null=False)
    address = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'

class PaymentType(models.Model):
    """
    Clase que gestiona los métodos de pago disponibles
    """
    pay_name = models.CharField(max_length=30, null=False, unique=True)

    def __str__(self) -> str:
        return f'{self.pay_name}'

class Order(models.Model):
    """
    Orden de compra, para todas las transacciones finalizadas
    """
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey('Customer', on_delete=models.PROTECT)
    country = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=120, null=False)
    method_payment = models.ForeignKey('PaymentType', on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    bikes = models.ManyToManyField('Bike', through='OrderBike')
    accessories = models.ManyToManyField('Accessories', through='OrderAccessories')

    @classmethod
    def create_from_cart(cls, client, cart, country, city, address, method_payment):
        order = cls(client=client, country=country, city=city, address=address, method_payment=method_payment)
        order.subtotal = cart.calculate_subtotal()
        order.save()
        for item in cart.items:
            if isinstance(item['product'], Bike):
                OrderBike.objects.create(order=order, bike=item['product'], quantity=item['quantity'])
            elif isinstance(item['product'], Accessories):
                OrderAccessories.objects.create(order=order, accessories=item['product'], quantity=item['quantity'])
        return order

    def __str__(self) -> str:
        return f'Orden de {self.client} - {self.date}'

class OrderBike(models.Model):
    """
    Modelo intermedio para gestionar las bicicletas en la orden.
    """
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    bike = models.ForeignKey('Bike', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ('order', 'bike')

class OrderAccessories(models.Model):
    """
    Modelo intermedio para gestionar los accesorios en la orden.
    """
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    accessories = models.ForeignKey('Accessories', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ('order', 'accessories')
class Cart:
    """
    Clase que gestiona todos los productos seleccionados por el titular.
    Es no persistente, por lo que no debería almacenarse en la bd.
    """
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        """
        Agrega productos al carrito
        """
        if not isinstance(product, Product):
            raise TypeError('El producto debe ser una instancia de la clase Product')
        for item in self.items:
            if item['product'] == product:
                item['quantity'] += quantity
                break
        else:
            self.items.append({'product': product, 'quantity': quantity})

    def remove_item(self, product):
        """
        Elimina un producto del carrito.
        """
        self.items = [item for item in self.items if item['product'] != product]

    def calculate_subtotal(self):
        """
        Calcula el subtotal basado en los productos y sus cantidades en el carrito.
        """
        subtotal = Decimal('0.00')
        for item in self.items:
            subtotal += item['product'].price * item['quantity']
        return subtotal

    def clear(self):
        """
        Vacía el carrito.
        """
        self.items = []
