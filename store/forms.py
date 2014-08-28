from django import forms
from django.core.exceptions import ValidationError

from store.models import Product, Cart 
EMPTY_FIELD_ERROR ="This field is required."
NEGATIVE_FIELD_ERROR = "Field must have a positive value"
VALUE_TO_BIG_ERROR = "Field value must be under quantity value"


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()
    prod_id = forms.IntegerField(widget=forms.HiddenInput())
    
    def clean_quantity(self):
        quantity=int(self.data['quantity'])
        prod_id =int(self.data['prod_id'])
        if quantity < 0:
            raise ValidationError(NEGATIVE_FIELD_ERROR)
        prod_quant = Product.objects.get(pk=prod_id).quantity
        if quantity > prod_quant:
            raise ValidationError(VALUE_TO_BIG_ERROR)
        return quantity
    
    def is_valid(self):
        prod_id =int(self.data['prod_id'])
        try:
            Product.objects.get(pk=prod_id)
        except Product.DoesNotExist:
            return False
        return super(AddToCartForm, self).is_valid()
    
    def save(self, key):
        return Cart.create_new(key=key, quantity=int(self.data['quantity']), prod_id=int(self.data['prod_id'])) 
            
