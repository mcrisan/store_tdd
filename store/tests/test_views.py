'''
Created on Aug 27, 2014

@author: mcrisan
'''
from django.test import TestCase

from store.models import Product, Cart
from store.forms import AddToCartForm


class HomePageTest(TestCase): 
    
    def setup(self):
        Product.objects.create(name="milk", quantity=5, price=2)

    def test_home_page_renders_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        
    def test_list_of_products_sent_to_template(self):
        Product.objects.create(name="p", price=1)
        products = Product.objects.all()
        response = self.client.get('/')
        self.assertEqual(len(response.context['products']), len(products))
        
    def test_form_sent_to_template(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], AddToCartForm)
    
    def test_POST_redirects_to_cart_view(self):
        product = Product.objects.create(name="salt", quantity=5, price=2)

        response = self.client.post(
            '/',
            data={'quantity': '1', 'prod_id': product.id }
        )
        cart = Cart.objects.first()
        self.assertRedirects(response, '/cart/%d/' % (cart.id,) )
        
    def test_POST_success_modifies_product_quantity(self):
        product = Product.objects.create(name="salt", quantity=5, price=2)
        ordered_quantity = 2
        self.client.post(
            '/',
            data={'quantity': ordered_quantity, 'prod_id': product.id }
        )
        new_quant = Product.objects.get(pk=product.id).quantity
        self.assertEqual(new_quant, product.quantity - ordered_quantity )


class CartPageTest(TestCase): 
    
    def test_home_page_renders_template(self):
        cart = Cart.objects.create(key="1")
        response = self.client.get('/cart/%d/' % (cart.id,))
        self.assertTemplateUsed(response, 'cart.html')
        
    def test_form_sent_to_template(self):
        cart = Cart.objects.create(key="1")
        response = self.client.get('/cart/%d/' % (cart.id,))
        self.assertEqual(response.context['cart'], cart)