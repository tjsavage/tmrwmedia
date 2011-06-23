#!/usr/bin/env python
from project.models import Project
from project.groups.models import Group
from project.contacts.models import Contact
from project.schedule.models import *
from project.schedule.forms import *
from registration.models import RegistrationProfile
from accounts import models

from datetime import date

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
	return HttpResponse("Schedule Index")

def callsheet(request, project_id, year, month, day):
	project = get_object_or_404(Project, pk=project_id)
	
	the_day = date(int(year), int(month), int(day))
	if the_day >= project.start_date.date() and the_day <= project.end_date.date():
		day, created = Day.objects.get_or_create(date=the_day, project=project)
	else:
		day = None
	
	calltimes = {}
	contacts = Contact.objects.filter(project=project)
	contact_calltimes = {}
	for contact in contacts:
		if contact.group == None:
			contact_calltimes[contact] = day.calltime(contact=contact)
	calltimes["No Group"] = contact_calltimes
	
	groups = Group.objects.filter(project=project)
	for group in groups:
		contacts = Contact.objects.filter(project=project).filter(group=group)
		contact_calltimes = {}
		for contact in contacts:
			contact_calltimes[contact] = day.calltime(contact=contact)
		calltimes[group.name] = contact_calltimes
	
	
	
	logging.debug("\n\Calltimes: " + str(calltimes) + "\n\n")
		
	group_calltime_form = GroupCalltimeForm(initial={'date': the_day})
	individual_calltime_form = IndividualCalltimeForm(initial={'date': the_day})
	group_calltime_form.for_project(project_id)
	individual_calltime_form.for_project(project_id)
	
		
	return render_to_response('project/schedule/callsheet.html', {"day" : day,
																"project" : project,
																"calltimes" : calltimes,
																"group_calltime_form": group_calltime_form,
																"individual_calltime_form": individual_calltime_form},
																context_instance=RequestContext(request))