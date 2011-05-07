from django.db import models
from django.contrib.auth.models import User
from callsheet.models import Callsheet

class Project(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	owner = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.name
	
	def callsheets(self):
		return Callsheet.objects.filter(project=self.pk)
		
	def positions(self):
		return Position.objects.filter(project=self.pk)

class Position(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	project = models.ForeignKey(Project)
	
	def __unicode__(self):
		return self.name