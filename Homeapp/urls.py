from django.urls import path
from. import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart_view, name='cart'),
    path('payment/', views.payment_view, name='payment'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:index>/', views.remove_from_cart, name='remove_from_cart'),


]
