from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.ForeignKey(User)
	phone = models.CharField(blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])