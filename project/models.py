from django.db import models
from django.contrib.auth.models import User
from callsheet.models import Callsheet

class Project(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	owner = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.name


