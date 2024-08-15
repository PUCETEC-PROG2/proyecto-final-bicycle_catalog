from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, Bike, Accessories
from .forms import OrderForm, BikeForm, AccessoriesForm


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

def accessories_list(request):
    accessories = Accessories.objects.all()
    return render(request, 'accessories_list.html', {'accessories': accessories})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})