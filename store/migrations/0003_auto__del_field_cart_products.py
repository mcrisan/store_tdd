# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Cart.products'
        db.delete_column(u'store_cart', 'products_id')

        # Adding M2M table for field products on 'Cart'
        m2m_table_name = db.shorten_name(u'store_cart_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cart', models.ForeignKey(orm[u'store.cart'], null=False)),
            ('product', models.ForeignKey(orm[u'store.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cart_id', 'product_id'])


    def backwards(self, orm):
        # Adding field 'Cart.products'
        db.add_column(u'store_cart', 'products',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['store.Product']),
                      keep_default=False)

        # Removing M2M table for field products on 'Cart'
        db.delete_table(db.shorten_name(u'store_cart_products'))


    models = {
        u'store.cart': {
            'Meta': {'object_name': 'Cart'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['store.Product']", 'symmetrical': 'False'})
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