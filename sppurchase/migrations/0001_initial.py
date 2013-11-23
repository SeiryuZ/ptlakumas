# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Purchase'
        db.create_table(u'sppurchase_purchase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('factory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basicinfo.Factory'], on_delete=models.PROTECT)),
            ('request_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('request_approval', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('request_reject', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order_number', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True, null=True, blank=True)),
            ('cancel_flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('closed_flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('memo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'sppurchase', ['Purchase'])

        # Adding model 'PurchaseItems'
        db.create_table(u'sppurchase_purchaseitems', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('purchase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sppurchase.Purchase'], on_delete=models.PROTECT)),
            ('master_spare_parts', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sp_spareparts.MasterSpareParts'], on_delete=models.PROTECT)),
            ('requested_quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('unit_price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('additional_cost', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('approved_quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('memo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'sppurchase', ['PurchaseItems'])

        # Adding model 'PurchaseItemsDelivery'
        db.create_table(u'sppurchase_purchaseitemsdelivery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('purchase_items', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sppurchase.PurchaseItems'], on_delete=models.PROTECT)),
            ('delivery_date', self.gf('django.db.models.fields.DateField')()),
            ('delivered_quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('memo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'sppurchase', ['PurchaseItemsDelivery'])


    def backwards(self, orm):
        # Deleting model 'Purchase'
        db.delete_table(u'sppurchase_purchase')

        # Deleting model 'PurchaseItems'
        db.delete_table(u'sppurchase_purchaseitems')

        # Deleting model 'PurchaseItemsDelivery'
        db.delete_table(u'sppurchase_purchaseitemsdelivery')


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
        u'sppurchase.purchase': {
            'Meta': {'object_name': 'Purchase'},
            'cancel_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'closed_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'factory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['basicinfo.Factory']", 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'order_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'request_approval': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'request_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'request_reject': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'sppurchase.purchaseitems': {
            'Meta': {'object_name': 'PurchaseItems'},
            'additional_cost': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'approved_quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'master_spare_parts': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sp_spareparts.MasterSpareParts']", 'on_delete': 'models.PROTECT'}),
            'memo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'purchase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sppurchase.Purchase']", 'on_delete': 'models.PROTECT'}),
            'requested_quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'unit_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'sppurchase.purchaseitemsdelivery': {
            'Meta': {'object_name': 'PurchaseItemsDelivery'},
            'delivered_quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'delivery_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'purchase_items': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sppurchase.PurchaseItems']", 'on_delete': 'models.PROTECT'})
        }
    }

    complete_apps = ['sppurchase']