django-openlayers
=================

django-openayers aims to be a reusable django app that allows displaying
maps from files and other sources supported by the awesome OpenLayers library.
OpenLayers is also the library used by GeoDjango, the contributed gis application 
that comes with Django.

**This package is in an alpha stage, don't use it in production. I will hopefully
provide a more stable version very soon.**

One motivation for building this app is to be able to deploy easily kml, gml and
other map types in a django-cms plugin. 


Implemented Features
--------------------

current version: 0.0.1

* basic Map, VectorLayer and RasterLayer and UploadedFile models
* Raster Layers: OSM and Google (street, terrain, satellite, hybrid)
* Vector Layers: KML
* some map controls
* simple view and template for map
* basic django-admin Map editing interface, with preview
* serving uploaded files for map (kml, etc)


RoadMap/Planned Features
------------------------

planned version: 0.1.0

* layer ordering, with drag and drop in admin
* write documentation
* templatetags
* django-cms plugin: work is in progress. A very basic implementation is included.
* map extent, boundaries, ecc
* handle projections
* More Raster Layers
* More Vector Layers
* Popup support for vector layer
* Feature inspector for vector layers
* Cross-origin vector layer sources
* Automatic json layers (or other format) from selected GeoDjango models, with generic views
* Thematic mapping and legend for vector layers


Installation
------------

To be written.


Demo
----

The app comes with a demo django project and 
a demo_cms project that includes django-cms integration


Compatibility
-------------

The app is being developed for Django >= 1.3.1. I'm not checking compatibility with other
Django versions right now.


