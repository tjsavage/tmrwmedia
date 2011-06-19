from piston.handler import BaseHandler
from project.models import Project
from project.schedule.models import *
from project.groups.models import Group

from datetime import date, time

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
	model = GroupCalltime
	
	def read(self, request, project_id, calltime_id):
		if calltime_id:
			return GroupCalltime.objects.get(pk=calltime_id)
		
		return None
	
	def write(self, request, project_id):
		project = Project.objects.get(pk=project_id)	
	
		group_id = request.POST['group']
		group = Group.objects.get(pk=group_id)
		year = request.POST['year']
		month = request.POST['month']
		day = request.POST['day']
		hour = request.POST['hour']
		minute = request.POST['minute']
		
		date_object = Date(int(year), int(month), int(day))
		day_object, created = Day.objects.get_or_create(date=date_object, project=project)
		day_object.save()
		
		group_calltime, created = GroupCalltime.objects.get_or_create(project=project, day=day_object, group=group)
		
		time_object = time(int(hour), int(minute))
		group_calltime.time = time_object
		group_calltime.save()

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