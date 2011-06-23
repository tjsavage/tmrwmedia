from piston.handler import BaseHandler
from project.models import Project
from project.schedule.models import *
from project.groups.models import Group

from datetime import date, time
from dateutil import *

import logging

class ProjectHandler(BaseHandler):
	allowed_methods = ('GET',)
	model = Project
	
	def read(self, request, project_id=None):
		base = Project.objects
	
		if project_id:
			return base.get(pk=project_id)
		else:
			return base.all()

class GroupCalltimeHandler(BaseHandler):
	allowed_methods = ('GET', 'POST',)
	#model = GroupCalltime
	fields = ('group', 'date', 'time')
	
	#def read(self, request, project_id):
	#	logging.debug("\n\nRead\n")
	#	return GroupCalltime.objects.filter(project=Project.objects.get(pk=project_id))
	
	def write(self, request, project_id):
		"""
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
		group_calltime.time = time_object
		group_calltime.save()
		
		return group_calltime
		"""
		return None
"""
class IndividualCalltimeHandler(BaseHandler):
	allowed_methods = ('GET', 'POST',)
	model = IndividualCalltime
	
	def read(self, request, project_id, calltime_id):
		if calltime_id:
			return GroupCalltime.objects.get(pk=calltime_id)
		
		return None
	
	def write(self, request, project_id):
		project = Project.objects.get(pk=project_id)	
	
		contact_id = request.POST['contact']
		contact = Contact.objects.get(pk=contact_id)
		year = request.POST['year']
		month = request.POST['month']
		day = request.POST['day']
		hour = request.POST['hour']
		minute = request.POST['minute']
		
		date_object = Date(int(year), int(month), int(day))
		day_object, created = Day.objects.get_or_create(date=date_object, project=project)
		day_object.save()
		
		individual_calltime, created = Individual.objects.get_or_create(project=project, day=day_object, contact=contact)
		
		time_object = time(int(hour), int(minute))
		individual_calltime.time = time_object
		individual_calltime.save()
"""