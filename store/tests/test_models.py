from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from store.models import Product, Cart

class ProductModelTest(TestCase):
    
    def test_save_product(self):
        prod = Product.objects.create(name="Milk", price=1)
        product = Product.objects.first()
        self.assertEqual(prod, product)
        
    def test_product_empty_string_name_not_saved(self):
        product = Product(name="", price=1)
        with self.assertRaises(ValidationError):
            product.save()
            product.full_clean()
            
    def test_product_duplicate_name_not_saved(self):
        product = Product(name="m", price=1)
        product.save()
        product2 = Product(name="m", price=1)
        with self.assertRaises(IntegrityError):
            product2.save()
            
    def test_modify_quantity(self):
        product = Product(name="m", quantity=5, price=1)
        product.save()
        product.modify_quantity(2)
        prod = Product.objects.first()
        self.assertEqual(product, prod)
        
        
class CartModelTest(TestCase): 
    
    def test_get_absolute_url(self):
        cart = Cart.objects.create(key="1")
        self.assertEqual(cart.get_absolute_url(), '/cart/%d/' % (cart.id,))
    
    def test_save_cart(self):
        prod = Product.objects.create(name="Milk", price=1)
        cart = Cart.objects.create(key="1")
        cart.products.add(prod)
        cart.save()
        cart = Cart.objects.first()
        self.assertEqual(cart.products.first(), prod)
        
    def test_create_new(self):
        prod = Product.objects.create(name="Milk", quantity=10, price=1)
        Cart.create_new(key='1', quantity=2, prod_id=prod.id) 
        cart = Cart.objects.first()
        self.assertEqual(cart.products.first(), prod)   
        
    def test_create_new_modifies_product_quantity(self):
        prod = Product.objects.create(name="Milk", quantity=10, price=1)
        ordered_quantity = 3
        Cart.create_new(key='1', quantity=ordered_quantity, prod_id=prod.id) 
        cart = Cart.objects.first()
        self.assertEqual(cart.products.first().quantity, prod.quantity-ordered_quantity)     