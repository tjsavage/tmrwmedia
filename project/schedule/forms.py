from project.schedule.models import *

from django import forms

class GroupCalltimeForm(forms.Form):
	group = forms.ModelChoiceField(Group.objects.all())
	time = forms.TimeField()
	date = forms.DateField(widget=forms.HiddenInput())
	
	
	def for_project(self, project_id=0):
		if project_id > 0:
			self.fields['group'].queryset = Group.objects.filter(project=project_id)
	
	def for_date(self, date):
		self.date = date

class IndividualCalltimeForm(forms.Form):
	contact = forms.ModelChoiceField(Contact.objects.all())
	time = forms.TimeField()
	date = forms.DateField(widget=forms.HiddenInput())
	
	def for_project(self, project_id):
		if project_id > 0:
			self.fields['contact'].queryset = Contact.objects.filter(project=project_id)
	