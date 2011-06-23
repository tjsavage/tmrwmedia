from django.db import models
from django.contrib.auth.models import User
from project.models import Project
from project.groups.models import Group

class Contact(models.Model):
	user = models.ForeignKey(User)
	first_name = models.CharField(max_length=30, blank=True, verbose_name = "First Name")
	last_name = models.CharField(max_length=30, blank=True, verbose_name = "Last Name")
	phone = models.CharField(max_length=30, blank=True, verbose_name = "Phone")
	email = models.CharField(max_length=40, blank=True, verbose_name = "Email")
	project = models.ForeignKey(Project)
	group = models.ForeignKey(Group, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.user.first_name + " " + self.user.last_name
		
	def __init__(self, *args, **kwargs):
		super(Contact, self).__init__(*args, **kwargs)
		self.first_name = self.user.first_name
		self.last_name = self.user.last_name
		self.phone = self.user.profile.phone
		self.email = self.user.email
		
	name = property(lambda s: s.first_name + " " + s.last_name)
	