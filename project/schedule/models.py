from project.models import Project
from project.groups.models import Group
from project.contacts.models import Contact

from django.db import models
from django.contrib.auth.models import User

class Day(models.Model):
	project = models.ForeignKey(Project)
	date = models.DateTimeField()
	notes = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.project.name + " : " + str(self.date)
		
	def calltime(self, user=None, contact=None):
		if not contact:
			contact = Contact.objects.filter(user=user).filter(project=self.project)[0]
		individual_calltime = IndividualCalltime.objects.filter(day=self).filter(user=user)
		if individual_calltime.count():
			return individual_calltime[0]
		
		group_calltime = GroupCalltime.objects.filter(day=self).filter(group=contact.group)
		if group_calltime.count():
			return group_calltime[0]
		
		return None
	
	def calltimes(self):
		contacts = Contacts.object.filter(project=self.project)
		calltimes = {}
		
		for contact in contacts:
			calltimes[contact] = self.calltime(contact = contact)
		
		return calltimes
		
		

class Calltime(models.Model):
	project = models.ForeignKey(Project)
	day = models.ForeignKey(Day)
	time = models.TimeField(blank=True)
	last_updated = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True
		
class GroupCalltime(Calltime):
	group = models.ForeignKey(Group)	
	
	def __unicode__(self):
		return self.project.name + ", " + self.group.name + " for " + str(self.day.date) + " at " + str(self.time)
		
class IndividualCalltime(Calltime):
	user = models.ForeignKey(User)
	
	def contact(self):
		return Contact.objects.filter(user=self.user).filter(project=self.project)[0]
		
	def __unicode__(self):
		return self.user.first_name + " " + self.user.last_name + " on " + str(self.day.date) + " at " + str(self.time)
		