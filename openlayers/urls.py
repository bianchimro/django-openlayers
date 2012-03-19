from django.conf.urls.defaults import *
import openlayers.views


urlpatterns = patterns('openlayers.views',
    (r'^map/(?P<id>\d+)/$', 'map'),
)



