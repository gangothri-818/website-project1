from django.shortcuts import render
from .models import ContactMessage



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

        # Save to DB
        ContactMessage.objects.create(name=name, email=email, message=message)
        message_sent = True

    return render(request, 'Pages/contact.html', {'message_sent': message_sent, 'name': name})


