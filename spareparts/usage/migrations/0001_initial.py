# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Adjustment'
        db.create_table(u'usage_adjustment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stock_spare_parts', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['master.StockSpareParts'], on_delete=models.PROTECT)),
            ('quantity', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('memo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'usage', ['Adjustment'])

        # Adding model 'Replacement'
        db.create_table(u'usage_replacement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stock_spare_parts', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['master.StockSpareParts'], on_delete=models.PROTECT)),
            ('machine_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basicinfo.MachineID'])),
            ('quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('memo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'usage', ['Replacement'])


    def backwards(self, orm):
        # Deleting model 'Adjustment'
        db.delete_table(u'usage_adjustment')

        # Deleting model 'Replacement'
        db.delete_table(u'usage_replacement')


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
        u'basicinfo.machineid': {
            'Meta': {'object_name': 'MachineID'},
            'factory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basicinfo.Factory']", 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'machine_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basicinfo.MachineType']", 'on_delete': 'models.PROTECT'})
        },
        u'basicinfo.machinetype': {
            'Meta': {'object_name': 'MachineType'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basicinfo.Department']", 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine_type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'master.masterspareparts': {
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
            'spareparts_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['master.SparePartsTypes']", 'on_delete': 'models.PROTECT'}),
            'supplier_code': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'master.sparepartstypes': {
            'Meta': {'object_name': 'SparePartsTypes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spareparts_type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'master.stockspareparts': {
            'Meta': {'object_name': 'StockSpareParts'},
            'factory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basicinfo.Factory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'master_spare_parts': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['master.MasterSpareParts']"}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'usage.adjustment': {
            'Meta': {'object_name': 'Adjustment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.SmallIntegerField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'stock_spare_parts': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['master.StockSpareParts']", 'on_delete': 'models.PROTECT'})
        },
        u'usage.replacement': {
            'Meta': {'object_name': 'Replacement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basicinfo.MachineID']"}),
            'memo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'stock_spare_parts': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['master.StockSpareParts']", 'on_delete': 'models.PROTECT'})
        }
    }

    complete_apps = ['usage']