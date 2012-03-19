# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Map'
        db.create_table('openlayers_map', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('openlayers', ['Map'])

        # Adding model 'RasterLayer'
        db.create_table('openlayers_rasterlayer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('openlayers', ['RasterLayer'])

        # Adding model 'VectorLayer'
        db.create_table('openlayers_vectorlayer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('openlayers', ['VectorLayer'])

        # Adding model 'MapsRasterLayers'
        db.create_table('openlayers_mapsrasterlayers', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openlayers.Map'])),
            ('layer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openlayers.RasterLayer'])),
        ))
        db.send_create_signal('openlayers', ['MapsRasterLayers'])

        # Adding model 'MapsVectorLayers'
        db.create_table('openlayers_mapsvectorlayers', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openlayers.Map'])),
            ('layer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openlayers.VectorLayer'])),
        ))
        db.send_create_signal('openlayers', ['MapsVectorLayers'])


    def backwards(self, orm):
        
        # Deleting model 'Map'
        db.delete_table('openlayers_map')

        # Deleting model 'RasterLayer'
        db.delete_table('openlayers_rasterlayer')

        # Deleting model 'VectorLayer'
        db.delete_table('openlayers_vectorlayer')

        # Deleting model 'MapsRasterLayers'
        db.delete_table('openlayers_mapsrasterlayers')

        # Deleting model 'MapsVectorLayers'
        db.delete_table('openlayers_mapsvectorlayers')


    models = {
        'openlayers.map': {
            'Meta': {'object_name': 'Map'},
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'openlayers.vectorlayer': {
            'Meta': {'object_name': 'VectorLayer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['openlayers']
