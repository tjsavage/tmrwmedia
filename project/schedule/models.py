from project.models import Project
from project.groups.models import Group
from project.contacts.models import Contact

from django.db import models
from django.contrib.auth.models import User

class Day(models.Model):
	project = models.ForeignKey(Project)
	date = models.DateField()
	notes = models.TextField(blank=True)

	
	def __unicode__(self):
		return self.project.name + " : " + str(self.date)
		
	def year(self):
		return self.date.year
	
	def month(self):
		return self.date.month
		
	def day(self):
		return self.date.day
	
	def title(self):
		return self.project.name + " " + str(self.date)
		
	def calltime(self, user=None, contact=None):
		if not contact:
			contact = Contact.objects.filter(user=user).filter(project=self.project)[0]
		individual_calltime = IndividualCalltime.objects.filter(day=self).filter(contact=contact)
		if individual_calltime.count():
			return individual_calltime[0]
		
		group_calltime = GroupCalltime.objects.filter(day=self).filter(group=contact.group)
		if group_calltime.count():
			return group_calltime[0]
		
		return None
	
	def calltimes(self):
		contacts = Contact.objects.filter(project=self.project)
		calltimes = {}
		
		for contact in contacts:
			calltimes[contact] = self.calltime(contact = contact)
		
		return calltimes
		
		

class Calltime(models.Model):
	project = models.ForeignKey(Project)
	day = models.ForeignKey(Day)
	time = models.TimeField(blank=True, null=True)
	last_updated = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True
		
class GroupCalltime(Calltime):
	group = models.ForeignKey(Group)	
	
	def __unicode__(self):
		return self.project.name + ", " + self.group.name + " for " + str(self.day.date) + " at " + str(self.time)
		
class IndividualCalltime(Calltime):
	contact = models.ForeignKey(Contact)
	
	def __unicode__(self):
		return self.contact.first_name + " " + self.contact.last_name + " on " + str(self.day.date) + " at " + str(self.time)
		