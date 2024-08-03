from django.db import models

"""
a landing page in Django. Basically, the home page will feature a brief description of VF Labs,
and then showcase 3 products, have tabs that correspond to the services offered 
by VF Labs(i.e Projects(current, future - ), Funding opportunities , consultancy),
and it will also have a contact us. """

class VflabsHome(models.Model):
    pass

class Project(models.Model):
    """showcases current and future projects"""
    STATUS_CHOICES = (
        ('current', 'current'),
        ('future', 'future'),
    )
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)  # Add a likes field
    # image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    def __str__(self):
        return self.name
    
class Service(models.Model):
    """showcases funding opportunities, consultancy, etc."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.subject
    
