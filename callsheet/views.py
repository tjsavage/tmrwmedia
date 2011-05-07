from callsheet.models import Callsheet
from callsheet.forms import *

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.context_processors import csrf
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse, HttpResponseRedirect



def index(request):
	callsheets = Callsheet.objects.filter(owner=request.user)

	return render_to_response('callsheet/index.html', {'callsheets' : callsheets}, context_instance=RequestContext(request))

def detail(request, callsheet_id):
	callsheet = get_object_or_404(Callsheet, pk=callsheet_id)

	return render_to_response('callsheet/detail.html', {'callsheet' : callsheet}, context_instance=RequestContext(request))
	
def new(request):
	
	class RequiredFormSet(BaseFormSet):
		def __init__(self, *args, **kwargs):
			super(RequiredFormSet, self).__init__(*args, **kwargs)
			for form in self.forms:
				form.empty_permitted = False
	
	ContactFormSet = formset_factory(ContactForm, formset=RequiredFormSet)
	
	if request.method == 'POST':
		callsheet_form = CallsheetForm(request.POST, request.FILES)
		contact_formset = ContactFormSet(request.POST, request.FILES)
		
		if callsheet_form.is_valid() and contact_formset.is_valid():
			callsheet = callsheet_form.save(commit=False)
			callsheet.owner = request.user
			callsheet.save()
			
			for form in contact_formset.forms:
				contact = form.save(commit=False)
				contact.callsheet = callsheet
				contact.save()
			
			return HttpResponseRedirect('/callsheets/')
	else:
		callsheet_form = CallsheetForm()
		contact_formset = ContactFormSet()
	
	c = {'callsheet_form':callsheet_form,
		'contact_formset': contact_formset}
	c.update(csrf(request))
	
	return render_to_response('callsheet/new.html', c, context_instance=RequestContext(request))