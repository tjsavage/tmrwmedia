from project.models import Project
from project.groups.models import Group
from project.contacts.forms import InviteForm
from project.contacts.models import Contact

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.context_processors import csrf
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request, project_id):
	contacts = Contact.objects.filter(project=project_id)
	invite_form = InviteForm()
	invite_form.for_project(project_id)

	return render_to_response('project/contacts/index.html',
								{ "contacts" : contacts,
								"invite_form" : invite_form
								}
								)

def invite(request, project_id):
	if request.method == "POST":
		form = InviteForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			group = form.cleaned_data['group']
			
	else:
		form = InviteForm()
		form.for_project(project_id)
	
	return render_to_response('project/contacts/invite.html', { "form" : form} )
		
		
