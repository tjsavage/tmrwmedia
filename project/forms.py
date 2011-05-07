from project.models import *
from django.forms import ModelForm

class ProjectForm(ModelForm):
	class Meta:
		model = Project
		exclude = ('owner',)