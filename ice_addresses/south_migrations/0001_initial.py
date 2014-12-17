# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PostCode'
        db.create_table(u'ice_addresses_postcode', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
        ))
        db.send_create_signal(u'ice_addresses', ['PostCode'])

        # Adding model 'Street'
        db.create_table(u'ice_addresses_street', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postcode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ice_addresses.PostCode'])),
            ('name_nominative', self.gf('django.db.models.fields.CharField')(max_length=48, db_index=True)),
            ('name_genitive', self.gf('django.db.models.fields.CharField')(max_length=48, db_index=True)),
        ))
        db.send_create_signal(u'ice_addresses', ['Street'])

        # Adding model 'Address'
        db.create_table(u'ice_addresses_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ice_addresses.Street'])),
            ('house_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('house_characters', self.gf('django.db.models.fields.CharField')(default=u'', max_length=3)),
            ('lon', self.gf('django.db.models.fields.FloatField')()),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'ice_addresses', ['Address'])


    def backwards(self, orm):
        # Deleting model 'PostCode'
        db.delete_table(u'ice_addresses_postcode')

        # Deleting model 'Street'
        db.delete_table(u'ice_addresses_street')

        # Deleting model 'Address'
        db.delete_table(u'ice_addresses_address')


    models = {
        u'ice_addresses.address': {
            'Meta': {'object_name': 'Address'},
            'house_characters': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '3'}),
            'house_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lon': ('django.db.models.fields.FloatField', [], {}),
            'street': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ice_addresses.Street']"})
        },
        u'ice_addresses.postcode': {
            'Meta': {'object_name': 'PostCode'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'ice_addresses.street': {
            'Meta': {'object_name': 'Street'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_genitive': ('django.db.models.fields.CharField', [], {'max_length': '48', 'db_index': 'True'}),
            'name_nominative': ('django.db.models.fields.CharField', [], {'max_length': '48', 'db_index': 'True'}),
            'postcode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ice_addresses.PostCode']"})
        }
    }

    complete_apps = ['ice_addresses']
