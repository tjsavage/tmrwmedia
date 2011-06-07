from django.conf.urls.defaults import *

urlpatterns = patterns('project.groups.views',
	(r'^$', 'index'),
	(r'^edit/$', 'edit'),
)