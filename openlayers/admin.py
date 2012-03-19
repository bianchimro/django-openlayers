from django.contrib import admin
from models import *


class RasterLayerAdminInline(admin.StackedInline):

    model = MapsRasterLayers 
    extra = 0


class VectorLayerAdminInline(admin.StackedInline):

    model = MapsVectorLayers 
    extra = 0


class MapAdmin(admin.ModelAdmin):
    
    model = Map
    inlines = [RasterLayerAdminInline, VectorLayerAdminInline]



admin.site.register(Map, MapAdmin)
admin.site.register(RasterLayer)
admin.site.register(VectorLayer)
admin.site.register(UploadedFile)
