# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Machine'
        db.delete_table(u'basicinfo_machine')

        # Adding model 'MachineType'
        db.create_table(u'basicinfo_machinetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basicinfo.Department'], on_delete=models.PROTECT)),
            ('machine_type', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
        ))
        db.send_create_signal(u'basicinfo', ['MachineType'])

        # Adding unique constraint on 'Factory', fields ['code_name']
        db.create_unique(u'basicinfo_factory', ['code_name'])

        # Deleting field 'MachineID.department'
        db.delete_column(u'basicinfo_machineid', 'department_id')

        # Adding field 'MachineID.machine_type'
        db.add_column(u'basicinfo_machineid', 'machine_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['basicinfo.MachineType'], on_delete=models.PROTECT),
                      keep_default=False)

        # Adding field 'MachineID.machine_number'
        db.add_column(u'basicinfo_machineid', 'machine_number',
                      self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=20),
                      keep_default=False)

        # Adding unique constraint on 'Department', fields ['department_name']
        db.create_unique(u'basicinfo_department', ['department_name'])

        # Adding unique constraint on 'Basic', fields ['company_name']
        db.create_unique(u'basicinfo_basic', ['company_name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Basic', fields ['company_name']
        db.delete_unique(u'basicinfo_basic', ['company_name'])

        # Removing unique constraint on 'Department', fields ['department_name']
        db.delete_unique(u'basicinfo_department', ['department_name'])

        # Removing unique constraint on 'Factory', fields ['code_name']
        db.delete_unique(u'basicinfo_factory', ['code_name'])

        # Adding model 'Machine'
        db.create_table(u'basicinfo_machine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('machine_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'basicinfo', ['Machine'])

        # Deleting model 'MachineType'
        db.delete_table(u'basicinfo_machinetype')


        # User chose to not deal with backwards NULL issues for 'MachineID.department'
        raise RuntimeError("Cannot reverse this migration. 'MachineID.department' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'MachineID.department'
        db.add_column(u'basicinfo_machineid', 'department',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['basicinfo.Department'], on_delete=models.PROTECT),
                      keep_default=False)

        # Deleting field 'MachineID.machine_type'
        db.delete_column(u'basicinfo_machineid', 'machine_type_id')

        # Deleting field 'MachineID.machine_number'
        db.delete_column(u'basicinfo_machineid', 'machine_number')


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