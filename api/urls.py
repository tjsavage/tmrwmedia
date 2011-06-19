from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import ProjectHandler

project_handler = Resource(ProjectHandler)

urlpatterns = patterns('',
	url(r'^projects/(?P<project_id>[^/]+)/', project_handler),
	url(r'^projects/', project_handler),
)