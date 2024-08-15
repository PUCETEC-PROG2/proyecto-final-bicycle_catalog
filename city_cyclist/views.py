from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, Bike, Accessories, Customer
from .forms import OrderForm, BikeForm, AccessoriesForm, CustomerForm
from .models import Cart

def add_bike_to_cart(request, bike_id):
    bike = get_object_or_404(Bike, id=bike_id)
    cart = Cart(request)
    cart.add_item(bike)
    return redirect('cart_detail')

def add_accessory_to_cart(request, accessory_id):
    accessory = get_object_or_404(Accessories, id=accessory_id)
    cart = Cart(request)
    cart.add_item(accessory)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})

def index(request):
    return render(request, 'index.html', {})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'order_detail.html', {'order': order})

def bike_list(request):
    bikes = Bike.objects.all()
    return render(request, 'bike_list.html', {'bikes': bikes})

def bike_detail(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    return render(request, 'bike_detail.html', {'bike': bike})

def bike_create(request):
    if request.method == 'POST':
        form = BikeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bike_list')
    else:
        form = BikeForm()
    return render(request, 'bike_form.html', {'form': form})

def bike_edit(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    if request.method == 'POST':
        form = BikeForm(request.POST, instance=bike)
        if form.is_valid():
            form.save()
            return redirect('bike_list')
    else:
        form = BikeForm(instance=bike)
    return render(request, 'bike_form.html', {'form': form})

def accessories_list(request):
    accessories = Accessories.objects.all()
    return render(request, 'accessories_list.html', {'accessories': accessories})

def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            client = form.cleaned_data['client']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            address = form.cleaned_data['address']
            method_payment = form.cleaned_data['method_payment']
            order = Order.create_from_cart(client, cart, country, city, address, method_payment)
            cart.clear()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_form.html', {'form': form})