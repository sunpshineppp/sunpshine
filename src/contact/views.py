from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact(request):
	title = "yaya"

	form = ContactForm(request.POST or None)
	if form.is_valid():
		instance = form.save()

	context = {
		"title": title,
		"form": form
	}
	return render(request, "contact.html", context)