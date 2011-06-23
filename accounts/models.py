from django.db import models
from django.contrib.auth.models import User
from project.models import Project

class UserProfile(models.Model):
	user = models.ForeignKey(User)
	phone = models.CharField(blank=True, max_length=12)
	date_added = models.DateTimeField(auto_now_add=True)

	def projects(self):
		return Project.objects.filter(owner=self.user)
	

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])