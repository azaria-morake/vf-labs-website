from django.contrib import admin
from .models import Project, Service, ContactUs, Investment

@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(Project)
admin.site.register(Service)
admin.site.register(ContactUs)
