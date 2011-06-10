from django.conf.urls.defaults import *

urlpatterns = patterns('project.views',
	(r'^$', 'index'),
	(r'^new/$', 'new'),
	(r'^(?P<project_id>\d+)/$', 'detail'),
	(r'^(?P<project_id>\d+)/edit/$', 'edit'),
	(r'^(?P<project_id>\d+)/groups/', include('project.groups.urls')),
	(r'^(?P<project_id>\d+)/contacts/', include('project.contacts.urls')),
	(r'^(?P<project_id>\d+)/callsheets/$', 'callsheets'),
)