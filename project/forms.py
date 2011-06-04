from project.models import *
from django.forms import ModelForm

class BasicProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = ('name',)