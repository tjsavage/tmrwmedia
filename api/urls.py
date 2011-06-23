from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import ProjectHandler, GroupCalltimeHandler
from api.views import groupcalltime

project_handler = Resource(ProjectHandler)

urlpatterns = patterns('',
	url(r'^projects/(?P<project_id>\d+)/$', project_handler),
	url(r'^projects/$', project_handler),
	url(r'^projects/(?P<project_id>\d+)/groupcalltime/$', 'api.views.groupcalltime'),
	url(r'^projects/(?P<project_id>\d+)/individualcalltime/$', 'api.views.individualcalltime'),
)