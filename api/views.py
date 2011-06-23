from project.models import Project
from project.schedule.models import *
from project.groups.models import Group

from datetime import date, time
from dateutil.parser import parse

from django.http import HttpResponse, HttpResponseRedirect

import logging

def groupcalltime(request, project_id):
	project = Project.objects.get(pk=project_id)	
	
	logging.debug("\n\nWriting group calltime\n\n")

	group_id = request.POST['group']
	group = Group.objects.get(pk=group_id)
	date = request.POST['date']
	time = request.POST['time']
	
	date_object = parse(date).date()
	day_object, created = Day.objects.get_or_create(date=date_object, project=project)
	day_object.save()
	
	group_calltime, created = GroupCalltime.objects.get_or_create(project=project, day=day_object, group=group)
	
	time_object = parse(time).time()
	
	logging.debug("\n\nTime: " + str(time_object) + " , " + str(time) + "\n\n")
	group_calltime.time = time_object
	group_calltime.save()
	
	return HttpResponseRedirect("/projects/" + str(project_id) + "/schedule/callsheet/" + str(date_object.year) + "/" + str(date_object.month) + "/" + str(date_object.day) + "/")

def individualcalltime(request, project_id):
	project = Project.objects.get(pk=project_id)	
	
	logging.debug("\n\nWriting group calltime\n\n")

	contact_id = request.POST['contact']
	contact = Contact.objects.get(pk=contact_id)
	date = request.POST['date']
	time = request.POST['time']
	
	date_object = parse(date).date()
	day_object, created = Day.objects.get_or_create(date=date_object, project=project)
	day_object.save()
	
	individual_calltime, created = IndividualCalltime.objects.get_or_create(project=project, day=day_object, contact=contact)
	
	time_object = parse(time).time()
	
	logging.debug("\n\nTime: " + str(time_object) + " , " + str(time) + "\n\n")
	individual_calltime.time = time_object
	individual_calltime.save()
	
	return HttpResponseRedirect("/projects/" + str(project_id) + "/schedule/callsheet/" + str(date_object.year) + "/" + str(date_object.month) + "/" + str(date_object.day) + "/")
