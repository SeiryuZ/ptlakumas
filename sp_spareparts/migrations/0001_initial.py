# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SparePartTypes'
        db.create_table(u'sp_spareparts_spareparttypes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('spareparts_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'sp_spareparts', ['SparePartTypes'])

        # Adding model 'MasterSpareParts'
        db.create_table(u'sp_spareparts_masterspareparts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('internal_code', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('supplier_code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('barcode', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('machine_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basicinfo.MachineType'], on_delete=models.PROTECT)),
            ('character', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('movability', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('chain_wheel_type', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('spareparts_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sp_spareparts.SparePartTypes'], on_delete=models.PROTECT)),
            ('natural_frequency', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('lifetime', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'sp_spareparts', ['MasterSpareParts'])


    def backwards(self, orm):
        # Deleting model 'SparePartTypes'
        db.delete_table(u'sp_spareparts_spareparttypes')

        # Deleting model 'MasterSpareParts'
        db.delete_table(u'sp_spareparts_masterspareparts')


    models = {
        u'basicinfo.department': {
            'Meta': {'object_name': 'Department'},
            'department_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'basicinfo.machinetype': {
            'Meta': {'object_name': 'MachineType'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basicinfo.Department']", 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'sp_spareparts.masterspareparts': {
            'Meta': {'object_name': 'MasterSpareParts'},
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'chain_wheel_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'character': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_code': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'lifetime': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'machine_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basicinfo.MachineType']", 'on_delete': 'models.PROTECT'}),
            'movability': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'natural_frequency': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'spareparts_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sp_spareparts.SparePartTypes']", 'on_delete': 'models.PROTECT'}),
            'supplier_code': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'sp_spareparts.spareparttypes': {
            'Meta': {'object_name': 'SparePartTypes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spareparts_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['sp_spareparts']