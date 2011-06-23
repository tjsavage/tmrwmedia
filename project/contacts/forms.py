from project.groups.models import Group
from project.contacts.models import Contact


from django import forms
from django.forms import ModelForm


class InviteForm(forms.Form):
	email = forms.CharField()
	first_name = forms.CharField()
	last_name = forms.CharField()
	phone = forms.CharField()
	group = forms.ModelChoiceField(Group.objects.all(), empty_label="None", required=False)
	
	def for_project(self, project_id=0):
		if project_id > 0:
			self.fields['group'].queryset = Group.objects.filter(project=project_id)
			
class ContactForm(ModelForm):
	#group = forms.ModelChoiceField(Group.objects.all(), empty_label="None", required=False)
	
	def for_project(self, project_id=0):
		if project_id > 0:
			self.fields['group'].queryset = Group.objects.filter(project=project_id)
	

	class Meta:
		model = Contact
		exclude = ('project', 'date_added', 'user',)