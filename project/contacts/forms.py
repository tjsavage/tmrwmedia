from project.groups.models import Group

from django import forms


class InviteForm(forms.Form):
	email = forms.CharField()
	first_name = forms.CharField()
	last_name = forms.CharField()
	group = forms.ModelChoiceField(Group.objects.none(), empty_label="None")
	
	def for_project(self, project_id=0):
		if project_id > 0:
			self.fields['group'].queryset = Group.objects.filter(project=project_id)
			
			