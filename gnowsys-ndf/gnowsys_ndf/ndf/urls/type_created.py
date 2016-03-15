from django.conf.urls import *
from django.conf.urls import patterns, url

urlpatterns = patterns('gnowsys_ndf.ndf.views.type_created',
                       url(r'^$', 'type_created', name='type_created'),


)