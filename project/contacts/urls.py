from django.conf.urls.defaults import *

urlpatterns = patterns('project.contacts.views',
	(r'^$', 'index'),
	(r'^invite/$', 'invite'),
	(r'^(?P<contact_id>\d+)/$', 'detail'),
	(r'^(?P<contact_id>\d+)/edit/', 'edit'),
)