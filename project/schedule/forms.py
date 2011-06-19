from project.schedule.models import *

from django import forms

class GroupCalltimeForm(forms.Form):
	group = forms.ModelChoiceField(Group.objects.all())
	time = forms.TimeField()
	
	
	def for_project(self, project_id=0):
		if project_id > 0:
			self.fields['group'].queryset = Group.objects.filter(project=project_id)