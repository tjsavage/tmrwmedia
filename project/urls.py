from django.conf.urls.defaults import *

urlpatterns = patterns('project.views',
	(r'^$', 'index'),
	(r'^new/$', 'new'),
	(r'^(?P<project_id>\d+)/detail$', 'detail'),
	(r'^(?P<project_id>\d+)/callsheets$', 'callsheets'),
)