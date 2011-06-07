from project.models import *
from django.forms import ModelForm

class BasicProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = ('name',) 

class ProjectForm(ModelForm):
	class Meta:
		model = Project
		exclude = ('owner', 'date_added', 'date_updated',)