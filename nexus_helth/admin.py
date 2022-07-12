from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(AppointmentBook)
class AppointmentBookAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'phone', 'requirements')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'phone', 'message')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('customer_name', 'designation', 'feedback')

admin.site.register(Banner)