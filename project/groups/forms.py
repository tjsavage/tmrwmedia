from django.forms import ModelForm

from project.models import *
from project.groups.models import Group

class GroupForm(ModelForm):
	class Meta:
		model = Group
		exclude = ('project',)