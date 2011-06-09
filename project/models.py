from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	location = models.TextField(blank=True)
	start_date = models.DateTimeField(null=True, blank=True)
	end_date = models.DateTimeField(null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True, null=True)
	owner = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.name

	def is_admin(self, user):
		if user == self.owner:
			return True
		return False
