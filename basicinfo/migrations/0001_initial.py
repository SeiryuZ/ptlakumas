# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Basic'
        db.create_table(u'basicinfo_basic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('ho_address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone1', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('phone2', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('phone3', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('fax1', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('fax2', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('fax3', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('email1', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('email2', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('email3', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'basicinfo', ['Basic'])

        # Adding model 'Factory'
        db.create_table(u'basicinfo_factory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'basicinfo', ['Factory'])

        # Adding model 'Department'
        db.create_table(u'basicinfo_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
        ))
        db.send_create_signal(u'basicinfo', ['Department'])

        # Adding model 'MachineType'
        db.create_table(u'basicinfo_machinetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basicinfo.Department'], on_delete=models.PROTECT)),
            ('machine_type', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
        ))
        db.send_create_signal(u'basicinfo', ['MachineType'])

        # Adding model 'MachineID'
        db.create_table(u'basicinfo_machineid', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('machine_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basicinfo.MachineType'], on_delete=models.PROTECT)),
            ('factory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basicinfo.Factory'], on_delete=models.PROTECT)),
            ('machine_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
        ))
        db.send_create_signal(u'basicinfo', ['MachineID'])


    def backwards(self, orm):
        # Deleting model 'Basic'
        db.delete_table(u'basicinfo_basic')

        # Deleting model 'Factory'
        db.delete_table(u'basicinfo_factory')

        # Deleting model 'Department'
        db.delete_table(u'basicinfo_department')

        # Deleting model 'MachineType'
        db.delete_table(u'basicinfo_machinetype')

        # Deleting model 'MachineID'
        db.delete_table(u'basicinfo_machineid')


    models = {
        u'basicinfo.basic': {
            'Meta': {'object_name': 'Basic'},
            'company_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'email1': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'email2': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'email3': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fax1': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'fax2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'fax3': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'ho_address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone1': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'phone2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'phone3': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
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
        }
    }

    complete_apps = ['basicinfo']