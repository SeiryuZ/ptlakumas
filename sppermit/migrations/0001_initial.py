# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Permit'
        db.create_table(u'sppermit_permit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('car_license', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('car_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('car_brand', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('driver', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('date_go', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'sppermit', ['Permit'])

        # Adding model 'PermitItems'
        db.create_table(u'sppermit_permititems', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('permit_number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sppermit.Permit'])),
            ('item', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('memo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'sppermit', ['PermitItems'])


    def backwards(self, orm):
        # Deleting model 'Permit'
        db.delete_table(u'sppermit_permit')

        # Deleting model 'PermitItems'
        db.delete_table(u'sppermit_permititems')


    models = {
        u'sppermit.permit': {
            'Meta': {'object_name': 'Permit'},
            'car_brand': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'car_license': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'car_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'date_go': ('django.db.models.fields.DateField', [], {}),
            'driver': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'sppermit.permititems': {
            'Meta': {'object_name': 'PermitItems'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'memo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'permit_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sppermit.Permit']"}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['sppermit']