# contact/models.py

from django.db import models

# Create your models here.

class ContactData(models.Model):
	email = models.EmailField(blank=False, null=False)
	full_name = models.CharField(max_length=40, default='', blank=False, null=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	message = models.TextField(max_length=2000, blank=False, null=False)

	def __str__(self):
		return self.email