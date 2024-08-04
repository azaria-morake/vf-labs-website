
from django.contrib import admin
from .models import Project, Service, ContactUs, Investment
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from .forms import SignUpForm

@csrf_exempt
def invest_sign_up(request):
    if request.method == 'POST':
        # Access form data
        name = request.POST.get('name')
        email = request.POST.get('email')
         # Save the data to the database
        investment = Investment(name=name, email=email)
        investment.save()
        
        # Return a JSON response
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def home(request):
    featured_projects = Project.objects.filter(featured=True)[:3]
    services = Service.objects.all()
    contact_details = {
        'email': 'info@vflabs.co.za',
        'phone': '+27 74 428 1408',
    }
    return render(request, 'home.html', {'projects': featured_projects, 'services': services, 'contact_details': contact_details})

def like_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.likes += 1
    project.save()
    return JsonResponse({'likes': project.likes})
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



