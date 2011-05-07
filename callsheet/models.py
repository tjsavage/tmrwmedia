from django.db import models
from django.contrib.auth.models import User

class Callsheet(models.Model):
	name = models.CharField(max_length=40)
	owner = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.name
		
	def contacts(self):
		contacts = Contact.objects.filter(callsheet=self.pk)
		return contacts
	
class Contact(models.Model):
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=14)
	callsheet = models.ForeignKey(Callsheet)
	
	def __unicode__(self):
		return self.name
	

