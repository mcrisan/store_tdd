from django.test import TestCase
from django.contrib.auth import SESSION_KEY

from store.forms import (
    AddToCartForm, 
    EMPTY_FIELD_ERROR, NEGATIVE_FIELD_ERROR, VALUE_TO_BIG_ERROR
    )
from store.models import Product, Cart

class AddToCartFormTest(TestCase):
    
    def test_form_render_hidden_product_id(self):
        form = AddToCartForm()
        self.assertIn('type="hidden"', form.as_p())
    
    def test_validation_for_blank_quantity(self):
        form = AddToCartForm(data={'quantity': '', 'prod_id':1})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['quantity'], [EMPTY_FIELD_ERROR])
        
    def test_validation_for_negative_quantity(self):
        form = AddToCartForm(data={'quantity': '-5', 'prod_id': '2'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['quantity'], [NEGATIVE_FIELD_ERROR])
        
    def test_validation_for_quantity_to_big(self):
        prod = Product.objects.create(name="milk", quantity=5, price=1)
        form = AddToCartForm(data={'quantity': '15', 'prod_id': prod.id})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['quantity'], [VALUE_TO_BIG_ERROR])
        
    def test_validation_product_id_not_found(self):
        form = AddToCartForm(data={'quantity': '15', 'prod_id': '2'})
        self.assertFalse(form.is_valid())
        
    def test_form_is_valid(self):
        prod = Product.objects.create(name="milk", quantity=5, price=1)
        form = AddToCartForm(data={'quantity': '1', 'prod_id': prod.id})
        self.assertTrue(form.is_valid())
        
    def test_save_creates_new_cart(self):
        product = Product.objects.create(name="salt", quantity=5, price=2)
        ordered_quantity = 2
        form = AddToCartForm(data={'quantity': ordered_quantity, 'prod_id': product.id})
        form.save(key=1)
        cart = Cart.objects.first()
        self.assertEqual(cart.products.first(), product)
        
    def test_save_returns_cart(self):
        product = Product.objects.create(name="salt", quantity=5, price=2)
        ordered_quantity = 2
        form = AddToCartForm(data={'quantity': ordered_quantity, 'prod_id': product.id})
        cart =form.save(key=1)
        cart = Cart.objects.first()
        self.assertEqual(cart, cart)