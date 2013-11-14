# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SparePartsTypes'
        db.create_table(u'sp_spareparts_sparepartstypes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('spareparts_type', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
        ))
        db.send_create_signal(u'sp_spareparts', ['SparePartsTypes'])

        # Adding model 'MasterSpareParts'
        db.create_table(u'sp_spareparts_masterspareparts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('internal_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=8)),
            ('supplier_code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('barcode', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('machine_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basicinfo.MachineType'], on_delete=models.PROTECT)),
            ('character', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('movability', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('chain_wheel_type', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('spareparts_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sp_spareparts.SparePartsTypes'], on_delete=models.PROTECT)),
            ('natural_frequency', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('lifetime', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'sp_spareparts', ['MasterSpareParts'])

        # Adding model 'StockSpareParts'
        db.create_table(u'sp_spareparts_stockspareparts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('factory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basicinfo.Factory'])),
            ('master_spare_parts', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sp_spareparts.MasterSpareParts'])),
            ('initial_quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'sp_spareparts', ['StockSpareParts'])


    def backwards(self, orm):
        # Deleting model 'SparePartsTypes'
        db.delete_table(u'sp_spareparts_sparepartstypes')

        # Deleting model 'MasterSpareParts'
        db.delete_table(u'sp_spareparts_masterspareparts')

        # Deleting model 'StockSpareParts'
        db.delete_table(u'sp_spareparts_stockspareparts')


    models = {
        u'basicinfo.department': {
            'Meta': {'object_name': 'Department'},
            'department_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'basicinfo.factory': {
            'Meta': {'object_name': 'Factory'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'code_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'basicinfo.machinetype': {
            'Meta': {'object_name': 'MachineType'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basicinfo.Department']", 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine_type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'sp_spareparts.masterspareparts': {
            'Meta': {'object_name': 'MasterSpareParts'},
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'chain_wheel_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'character': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '8'}),
            'lifetime': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'machine_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basicinfo.MachineType']", 'on_delete': 'models.PROTECT'}),
            'movability': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'natural_frequency': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'spareparts_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sp_spareparts.SparePartsTypes']", 'on_delete': 'models.PROTECT'}),
            'supplier_code': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'sp_spareparts.sparepartstypes': {
            'Meta': {'object_name': 'SparePartsTypes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spareparts_type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'sp_spareparts.stockspareparts': {
            'Meta': {'object_name': 'StockSpareParts'},
            'factory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basicinfo.Factory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'master_spare_parts': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sp_spareparts.MasterSpareParts']"}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['sp_spareparts']