from django.contrib import admin
from .models import ContactForm


@admin.register(ContactForm)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['username','email','password1','password2']