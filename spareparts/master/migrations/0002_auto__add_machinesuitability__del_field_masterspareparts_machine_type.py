# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MachineSuitability'
        db.create_table(u'master_machinesuitability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('master_spare_parts', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['master.MasterSpareParts'])),
            ('machine_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basicinfo.MachineType'], on_delete=models.PROTECT)),
        ))
        db.send_create_signal(u'master', ['MachineSuitability'])

        # Deleting field 'MasterSpareParts.machine_type'
        db.delete_column(u'master_masterspareparts', 'machine_type_id')


    def backwards(self, orm):
        # Deleting model 'MachineSuitability'
        db.delete_table(u'master_machinesuitability')


        # User chose to not deal with backwards NULL issues for 'MasterSpareParts.machine_type'
        raise RuntimeError("Cannot reverse this migration. 'MasterSpareParts.machine_type' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'MasterSpareParts.machine_type'
        db.add_column(u'master_masterspareparts', 'machine_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basicinfo.MachineType'], on_delete=models.PROTECT),
                      keep_default=False)


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
        u'master.machinesuitability': {
            'Meta': {'object_name': 'MachineSuitability'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basicinfo.MachineType']", 'on_delete': 'models.PROTECT'}),
            'master_spare_parts': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['master.MasterSpareParts']"})
        },
        u'master.masterspareparts': {
            'Meta': {'object_name': 'MasterSpareParts'},
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'chain_wheel_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'character': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '8'}),
            'lifetime': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
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
        }
    }

    complete_apps = ['master']