from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	name = models.CharField(max_length=40)
	date_added = models.DateTimeField(auto_now_add=True)