from django.conf.urls.defaults import *

urlpatterns = patterns('project.contacts.views',
	(r'^$', 'index'),
	(r'^invite/$', 'invite'),
)