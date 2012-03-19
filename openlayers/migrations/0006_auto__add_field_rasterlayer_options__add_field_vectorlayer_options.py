# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'RasterLayer.options'
        db.add_column('openlayers_rasterlayer', 'options', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'VectorLayer.options'
        db.add_column('openlayers_vectorlayer', 'options', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'RasterLayer.options'
        db.delete_column('openlayers_rasterlayer', 'options')

        # Deleting field 'VectorLayer.options'
        db.delete_column('openlayers_vectorlayer', 'options')


    models = {
        'openlayers.map': {
            'Meta': {'object_name': 'Map'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'openlayers.rasterlayer': {
            'Meta': {'object_name': 'RasterLayer'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maps': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'raster_layers'", 'symmetrical': 'False', 'to': "orm['openlayers.Map']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'options': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'openlayers.vectorlayer': {
            'Meta': {'object_name': 'VectorLayer'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maps': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'vector_layers'", 'symmetrical': 'False', 'to': "orm['openlayers.Map']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'options': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['openlayers']
