# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from . import rename_tables_new_to_old, rename_tables_old_to_new


class Migration(SchemaMigration):
    cms_plugin_table_mapping = (
        ('cmsplugin_grid', 'djangocms_grid_grid'),
        ('cmsplugin_gridcolumn', 'djangocms_grid_gridcolumn'),
    )

    def forwards(self, orm):
        rename_tables_old_to_new(db, self.cms_plugin_table_mapping)

    def backwards(self, orm):
        rename_tables_new_to_old(db, self.cms_plugin_table_mapping)


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'djangocms_grid.grid': {
            'Meta': {'object_name': 'Grid', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'custom_classes': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'inner': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'djangocms_grid.gridcolumn': {
            'Meta': {'object_name': 'GridColumn', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'custom_classes': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '50'})
        }
    }

    complete_apps = ['djangocms_grid']