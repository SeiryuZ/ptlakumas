# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SparepartsLog'
        db.create_table(u'logs_sparepartslog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('table_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('action_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('record_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('modified_by', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('modified_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'logs', ['SparepartsLog'])

        # Adding model 'BasicInfoLog'
        db.create_table(u'logs_basicinfolog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('table_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('action_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('record_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('modified_by', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('modified_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'logs', ['BasicInfoLog'])


    def backwards(self, orm):
        # Deleting model 'SparepartsLog'
        db.delete_table(u'logs_sparepartslog')

        # Deleting model 'BasicInfoLog'
        db.delete_table(u'logs_basicinfolog')


    models = {
        u'logs.basicinfolog': {
            'Meta': {'object_name': 'BasicInfoLog'},
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {}),
            'record_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'table_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'logs.sparepartslog': {
            'Meta': {'object_name': 'SparepartsLog'},
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {}),
            'record_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'table_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['logs']