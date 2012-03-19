django-openlayers
=================

django-openayers aims to be a reusable django app that allows displaying
maps from files and other sources supported by the awesome OpenLayers library.
OpenLayers is also the library used by GeoDjango, the contributed gis application 
that comes with Django.

**This package is in an alpha stage, don't use it in production. I will hopefully
provide a more stable version very soon.**

One motivation for building this app is to be able to deploy easily kml, gml and
other map types in a django-cms plugin (This feature is still to be implemented, but will come soon)


Implemented Features
--------------------

* basic Map, VectorLayer and RasterLayer and UploadedFile models
* Raster Layers: OSM and Google (street, terrain, satellite, hybrid)
* Vector Layers: KML
* simple view and template for map
* basic django-admin Map editing interface, with preview
* serving uploaded files for map (kml, etc)


RoadMap/Planned Features
------------------------

* templatetags
* django-cms plugin
* write documentation
* More Raster Layers
* More Vector Layers
* Popup support for vector layer
* Feature inspector for vector layer
* Cross-origin vector layer sources
* Automatic json layers (or other format) from selected GeoDjango models, with generic views


Installation
------------

To be written.


Demo
----

The app comes with a demo django project


Compatibility
-------------

The app is being developed for Django >= 1.3.1. I'm not checking compatibility with other
Django versions right now.


