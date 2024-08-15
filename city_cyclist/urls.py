from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/create/', views.create_order, name='create_order'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add_bike/<int:bike_id>/', views.add_bike_to_cart, name='add_bike_to_cart'),
    path('cart/add_accessory/<int:accessory_id>/', views.add_accessory_to_cart, name='add_accessory_to_cart'),
    path('bikes/', views.bike_list, name='bike_list'),
    path('bikes/<int:pk>/', views.bike_detail, name='bike_detail'),
    path('bikes/new/', views.bike_create, name='bike_create'),
    path('bikes/edit/<int:pk>/', views.bike_edit, name='bike_edit'),
    path('accessories/', views.accessories_list, name='accessories_list'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/new/', views.customer_create, name='customer_create'),
    path('customers/edit/<int:pk>/', views.customer_edit, name='customer_edit')
]