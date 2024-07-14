
from django.contrib import admin
from .models import Project, Service, ContactUs
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

def home(request):
    featured_projects = Project.objects.filter(featured=True)[:3]
    services = Service.objects.all()
    contact_details = {
        'email': 'info@vflabs.co.za',
        'phone': '+27 74 1408 428',
    }
    return render(request, 'home.html', {'projects': featured_projects, 'services': services, 'contact_details': contact_details})

""" 
Redundant contact form code:

@csrf_protect
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        
        return redirect('home')
    return render(request, 'contact.html') 

    """



