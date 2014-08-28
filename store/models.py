from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField(default=0)
    price = models.FloatField()
    
    def modify_quantity(self, quantity):
        self.quantity += quantity
        self.save()
    
class Cart(models.Model):
    key = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField(max_length=100, null=True, default=0)
    products = models.ManyToManyField(Product, null=True)
    
    def get_absolute_url(self):
        return reverse('view_cart', args=[self.id])
    
    @staticmethod
    def create_new(key, prod_id, quantity):
        product = Product.objects.get(pk=prod_id)
        cart = Cart.objects.create(key="1", quantity=2)
        cart.products.add(product)
        cart.save()
        product.modify_quantity(-quantity)
        return cart
        