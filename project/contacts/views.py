#!/usr/bin/env python
from project.models import Project
from project.groups.models import Group
from project.contacts.forms import InviteForm, ContactForm
from project.contacts.models import Contact
from registration.models import RegistrationProfile
from accounts import models

from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.template import RequestContext
from django.core.context_processors import csrf
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

import logging

def index(request, project_id):
	#print "HIHIIHIH"
	contacts = Contact.objects.filter(project=project_id)
	invite_form = InviteForm()
	invite_form.for_project(project_id)
	project = get_object_or_404(Project, pk=project_id)
	
	
	
	return render_to_response('project/contacts/index.html',
								{ "contacts" : contacts,
								"invite_form" : invite_form,
								"project" : project
								}, 
								context_instance=RequestContext(request)
								)

def edit(request, project_id, contact_id):
	project = get_object_or_404(Project, pk=project_id)
	contact = get_object_or_404(Contact, pk=contact_id)

	if request.method == "POST":
		logging.debug('\n\n POST: ' + str(request.POST) + " " + str(contact) + '\n\n')
		contact_form = ContactForm(instance=contact)
		logging.debug('\n\n' + str(contact_form) + '\n\n')
		
		logging.debug('\n\n' + str(contact_form) + '\n\n')
		
		if contact_form.is_valid():
			contact_form.save()
			return HttpResponseRedirect('/projects/' + str(project_id) + '/contacts/')
	else:
		contact_form = ContactForm(instance=contact)
		logging.debug('\n\n' + str(contact_form) + '\n\n')
		
	contact_form.for_project(project_id)
	
	return render_to_response('project/contacts/edit.html',
								{ "contact" : contact,
								"contact_form" : contact_form,
								"project" : project
								},
								context_instance=RequestContext(request)
								)

def detail(request, project_id, contact_id):
	return HttpResponse("detail")

def invite(request, project_id):
	logging.debug("This is a post \n")
	if request.method == "POST":
		form = InviteForm(request.POST)
		if form.is_valid():
			
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			group = form.cleaned_data['group']
			phone = form.cleaned_data['phone']
			
			
			
			if Site._meta.installed:
				site = Site.objects.get_current()
			else:
				site = RequestSite(request)
			new_user = RegistrationProfile.objects.create_inactive_user(email, email, "1234", site, False)
			
			new_user.first_name = first_name
			new_user.last_name = last_name
			new_user.save()
			prof = new_user.profile
			prof.phone = phone
			prof.save()
			
			contact = Contact(user=new_user, project=get_object_or_404(Project, pk=project_id))
			if group:
				contact.group = group
			
			contact.save()
			
			return HttpResponseRedirect("/projects/" + str(project_id) + "/contacts/")
			
	else:
		form = InviteForm()
	form.for_project(project_id)	
	
	return render_to_response('project/contacts/invite.html', { "form" : form}, 
								context_instance=RequestContext(request) )
		
		
