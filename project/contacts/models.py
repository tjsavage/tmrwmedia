from django.db import models
from django.contrib.auth.models import User
from project.models import Project
from project.groups.models import Group

class Contact(models.Model):
	user = models.ForeignKey(User)
	edited_first_name = models.CharField(blank=True)
	edited_last_name = models.CharField(blank=True)
	edited_phone = models.CharField(blank=True)
	edited_email = models.CharField(blank=True)
	project = models.ForeignKey(Project)
	group = models.ForeignKey(Group, null=True)
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.user.first_name + " " + self.user.last_name + " in " + self.project.name
		
	def get_first_name(self):
		if self.edited_first_name:
			return self.edited_first_name
		return self.user.first_name
	
	def set_first_name(self, fn):
		self.edited_first_name = fn
	
	def get_last_name(self):
		if self.edited_last_name:
			return self.edited_last_name
		return self.user.last_name
	
	def set_last_name(self, ln):
		self.edited_last_name = ln
		
	def get_phone(self):
		if self.edited_phone:
			return self.edited_phone
		return self.user.profile.phone
		
	def set_phone(self, ph):
		self.edited_phone = ph
	
	def get_email(self):
		if self.edited_email:
			return self.edited_email
		return self.user.email
	
	def set_email(self, em):
		self.edited_email = em
		
	
	first_name = property(get_first_name, set_first_name)
	last_name = property(get_last_name, set_last_name)
	phone = property(get_phone, set_phone)
	email = property(get_email, set_email)
	