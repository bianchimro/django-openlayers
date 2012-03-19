# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'MapsVectorLayers'
        db.delete_table('openlayers_mapsvectorlayers')

        # Deleting model 'MapsRasterLayers'
        db.delete_table('openlayers_mapsrasterlayers')

        # Adding field 'RasterLayer.map'
        db.add_column('openlayers_rasterlayer', 'map', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['openlayers.Map']), keep_default=False)

        # Adding field 'VectorLayer.map'
        db.add_column('openlayers_vectorlayer', 'map', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['openlayers.Map']), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'MapsVectorLayers'
        db.create_table('openlayers_mapsvectorlayers', (
            ('map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openlayers.Map'])),
            ('layer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openlayers.VectorLayer'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('openlayers', ['MapsVectorLayers'])

        # Adding model 'MapsRasterLayers'
        db.create_table('openlayers_mapsrasterlayers', (
            ('map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openlayers.Map'])),
            ('layer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openlayers.RasterLayer'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('openlayers', ['MapsRasterLayers'])

        # Deleting field 'RasterLayer.map'
        db.delete_column('openlayers_rasterlayer', 'map_id')

        # Deleting field 'VectorLayer.map'
        db.delete_column('openlayers_vectorlayer', 'map_id')


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
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['openlayers.Map']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'openlayers.vectorlayer': {
            'Meta': {'object_name': 'VectorLayer'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['openlayers.Map']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['openlayers']
