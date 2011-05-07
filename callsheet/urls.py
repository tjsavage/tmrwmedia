from django.conf.urls.defaults import *

urlpatterns = patterns('callsheet.views',
	(r'^$', 'index'),
	(r'^new/$', 'new'),
	(r'^(?P<callsheet_id>\d+)/detail$', 'detail'),
)