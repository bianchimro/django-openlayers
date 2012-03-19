from django.conf.urls.defaults import *
import openlayers.views
import settings


urlpatterns = patterns('openlayers.views',
    (r'^map/(?P<id>\d+)/$', 'map'),
)


urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + "openlayers"}),
)



