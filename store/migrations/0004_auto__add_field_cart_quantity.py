# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Cart.quantity'
        db.add_column(u'store_cart', 'quantity',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Cart.quantity'
        db.delete_column(u'store_cart', 'quantity')


    models = {
        u'store.cart': {
            'Meta': {'object_name': 'Cart'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['store.Product']", 'null': 'True', 'symmetrical': 'False'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '100', 'null': 'True'})
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