from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/create/', views.create_order, name='create_order'),
    path('bikes/', views.bike_list, name='bike_list'),
    path('accessories/', views.accessories_list, name='accessories_list'),
]