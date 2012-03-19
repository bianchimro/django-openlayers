# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Map.description'
        db.add_column('openlayers_map', 'description', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'RasterLayer.description'
        db.add_column('openlayers_rasterlayer', 'description', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'VectorLayer.description'
        db.add_column('openlayers_vectorlayer', 'description', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Map.description'
        db.delete_column('openlayers_map', 'description')

        # Deleting field 'RasterLayer.description'
        db.delete_column('openlayers_rasterlayer', 'description')

        # Deleting field 'VectorLayer.description'
        db.delete_column('openlayers_vectorlayer', 'description')


    models = {
        'openlayers.map': {
            'Meta': {'object_name': 'Map'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'openlayers.mapsrasterlayers': {
            'Meta': {'object_name': 'MapsRasterLayers'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['openlayers.RasterLayer']"}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['openlayers.Map']"})
        },
        'openlayers.mapsvectorlayers': {
            'Meta': {'object_name': 'MapsVectorLayers'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['openlayers.VectorLayer']"}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['openlayers.Map']"})
        },
        'openlayers.rasterlayer': {
            'Meta': {'object_name': 'RasterLayer'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'openlayers.vectorlayer': {
            'Meta': {'object_name': 'VectorLayer'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['openlayers']
