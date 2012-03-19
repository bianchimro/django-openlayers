# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'RasterLayer.map'
        db.delete_column('openlayers_rasterlayer', 'map_id')

        # Adding M2M table for field map on 'RasterLayer'
        db.create_table('openlayers_rasterlayer_map', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('rasterlayer', models.ForeignKey(orm['openlayers.rasterlayer'], null=False)),
            ('map', models.ForeignKey(orm['openlayers.map'], null=False))
        ))
        db.create_unique('openlayers_rasterlayer_map', ['rasterlayer_id', 'map_id'])

        # Deleting field 'VectorLayer.map'
        db.delete_column('openlayers_vectorlayer', 'map_id')

        # Adding M2M table for field map on 'VectorLayer'
        db.create_table('openlayers_vectorlayer_map', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vectorlayer', models.ForeignKey(orm['openlayers.vectorlayer'], null=False)),
            ('map', models.ForeignKey(orm['openlayers.map'], null=False))
        ))
        db.create_unique('openlayers_vectorlayer_map', ['vectorlayer_id', 'map_id'])


    def backwards(self, orm):
        
        # Adding field 'RasterLayer.map'
        db.add_column('openlayers_rasterlayer', 'map', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['openlayers.Map']), keep_default=False)

        # Removing M2M table for field map on 'RasterLayer'
        db.delete_table('openlayers_rasterlayer_map')

        # Adding field 'VectorLayer.map'
        db.add_column('openlayers_vectorlayer', 'map', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['openlayers.Map']), keep_default=False)

        # Removing M2M table for field map on 'VectorLayer'
        db.delete_table('openlayers_vectorlayer_map')


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
            'map': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['openlayers.Map']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'openlayers.vectorlayer': {
            'Meta': {'object_name': 'VectorLayer'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['openlayers.Map']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['openlayers']
