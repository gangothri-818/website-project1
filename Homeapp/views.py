from django.shortcuts import render,redirect
from .models import ContactMessage
import random
from django.contrib import messages



def home(request):
    return render(request, 'Pages/home.html')

def about(request):
    return render(request, 'Pages/about.html')

def services(request):
    return render(request, 'Pages/services.html')



def contact(request):
    message_sent = False
    name = ''

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(name=name, email=email, message=message)
        message_sent = True

    return render(request, 'Pages/contact.html', {'message_sent': message_sent, 'name': name})


def cart_view(request):
    cart = request.session.get('cart', [])
    total = sum(item['price'] for item in cart)
    return render(request, 'Pages/cart.html', {'cart': cart, 'total': total})


def payment_view(request):
    cart = request.session.get('cart', [])
    if not cart:
        return redirect('cart')  # Block access if cart is empty

    if request.method == 'POST':
        # Simulate successful payment
        request.session['cart'] = []
        return render(request, 'Pages/payment.html', {'message': 'Payment successful!', 'cart': []})

    return render(request, 'Pages/payment.html', {'cart': cart})



def add_to_cart(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = float(request.POST.get('price'))

        cart = request.session.get('cart', [])
        cart.append({'name': name, 'price': price})
        request.session['cart'] = cart

        messages.success(request, f"{name} added to cart!")
        
        return redirect(request.META.get('HTTP_REFERER', 'home'))  # Stay on same page

def remove_from_cart(request, index):
    cart = request.session.get('cart', [])
    try:
        cart.pop(index)
        request.session['cart'] = cart
    except IndexError:
        pass  # Just ignore if invalid index
    return redirect('cart')

