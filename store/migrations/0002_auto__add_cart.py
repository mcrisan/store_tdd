# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cart'
        db.create_table(u'store_cart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('products', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['store.Product'])),
        ))
        db.send_create_signal(u'store', ['Cart'])


    def backwards(self, orm):
        # Deleting model 'Cart'
        db.delete_table(u'store_cart')


    models = {
        u'store.cart': {
            'Meta': {'object_name': 'Cart'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'products': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Product']"})
        },
        u'store.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['store']