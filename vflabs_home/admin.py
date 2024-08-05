from django.contrib import admin
from .models import Project, Service, ContactUs, Investment

@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number')

admin.site.register(Project)
admin.site.register(Service)
admin.site.register(ContactUs)
