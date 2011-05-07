from callsheet.models import *
from django.forms import ModelForm

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		exclude = ('callsheet',)

class CallsheetForm(ModelForm):
	class Meta:
		model = Callsheet
		exclude = ('project', 'owner',)

