from django.db import models

import re
import unicodedata
import json

def getSlug(s):
    slug = unicodedata.normalize('NFKD', s)
    slug = slug.encode('ascii', 'ignore').lower()
    slug = re.sub(r'[^a-z0-9]+', '', slug).strip('-')
    slug = re.sub(r'[-]+', '', slug)
    return slug

VECTOR_LAYERS_TYPES = (
    ('kml', 'KML layer'),
    ('wfs', 'wfs layer'),
)

RASTER_LAYERS_TYPES = (
    ('OSM', 'OSM layer'),
    ('GOOGLE-STREET', 'Google street'),
    ('GOOGLE-SATELLITE', 'Google satellite'),
    ('GOOGLE-TERRAIN', 'Google terrain'),
    ('GOOGLE-HYBRID', 'Google hybrid'),
    
)

JS_BOOL_CHOICES = (
    ('true', 'True'),
    ('false', 'False'),
)



class Map(models.Model):
    
    name = models.CharField(null=False, blank=False, unique=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    navigation_control = models.BooleanField(default=True)
    layer_switcher_control = models.BooleanField(default=False)
    scale_line_control = models.BooleanField(default=False)
    pan_zoom_bar_control = models.BooleanField(default=False)
    
    def getDivId(self):
        return getSlug(self.name)
    
class _Layer(models.Model):

    name = models.CharField(null=False, blank=False, unique=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    options = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True
        
    def __unicode__(self):
        return u'%s' % (self.name)
        
        
class RasterLayer(_Layer):
    
    maps = models.ManyToManyField(Map, related_name='raster_layers', null=True, blank=True)
    type = models.CharField(max_length=300, choices = RASTER_LAYERS_TYPES)
    

class VectorLayer(_Layer):
    
    maps = models.ManyToManyField(Map, related_name='vector_layers', null=True, blank=True)
    type = models.CharField(max_length=300, choices = VECTOR_LAYERS_TYPES)
    layer_uri =  models.CharField(null=True, blank=True, max_length=300)
    
    #layer options
    extract_styles = models.CharField(choices = JS_BOOL_CHOICES, default="true", max_length=10);
    extract_attributes = models.CharField(choices = JS_BOOL_CHOICES, default="true", max_length=10);    
    
    #popup_handler = models.BooleanField(default=False)



class UploadedFile(models.Model):
    file = models.FileField(upload_to='openlayers')
    description = models.TextField(null=True, blank=True)


"""    
class MapsRasterLayers(models.Model):

    map = models.ForeignKey(Map)
    layer = models.ForeignKey(RasterLayer)
    

class MapsVectorLayers(models.Model):

    map = models.ForeignKey(Map)
    layer = models.ForeignKey(VectorLayer)
"""