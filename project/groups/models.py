from django.db import models
from django.contrib.auth.models import User

from project.models import Project

class Group(models.Model):
	name = models.CharField(max_length=40)
	leader = models.ForeignKey(User)
	project = models.ForeignKey(Project)
	
	def __unicode__(self):
		return self.name