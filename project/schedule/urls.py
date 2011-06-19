from django.conf.urls.defaults import *

urlpatterns = patterns('project.schedule.views',
	(r'^$', 'index'),
	(r'^callsheet/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', 'callsheet'),
)