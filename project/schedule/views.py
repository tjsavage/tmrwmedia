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
		
	group_calltime_form = GroupCalltimeForm()
	group_calltime_form.for_project(project_id)
	
		
	return render_to_response('project/schedule/callsheet.html', {"day" : day,
																"project" : project})