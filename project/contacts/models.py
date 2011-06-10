from django.db import models
from django.contrib.auth.models import User
from project.models import Project
from project.groups.models import Group

class Contact(models.Model):
	user = models.ForeignKey(User)
	project = models.ForeignKey(Project)
	group = models.ForeignKey(Group)
	date_added = models.DateTimeField(auto_now_add=True)
	
	