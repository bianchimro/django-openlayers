from cms.models.pluginmodel import CMSPlugin
from django.db import models
from openlayers.models import Map

class MapPluginModel(CMSPlugin):
    map = models.ForeignKey(Map)