from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^registration/', include('registration.backends.default.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^callsheets/', include('callsheet.urls')),
    (r'^projects/', include('project.urls')),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
)
