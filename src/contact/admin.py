from django.contrib import admin

# Register your models here.
from .forms import ContactForm
from .models import ContactData

class ContactDataAdmin(admin.ModelAdmin):
	list_display = ["__str__", "full_name", "timestamp"]
	form = ContactForm

admin.site.register(ContactData, ContactDataAdmin)
