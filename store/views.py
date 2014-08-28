from django.shortcuts import render, redirect

from store.models import Product, Cart
from store.forms import AddToCartForm

def home(request):
    form = AddToCartForm()
    products = Product.objects.all()
    print request.session.session_key
    if request.method == 'POST':
        form = AddToCartForm(data=request.POST)
        if form.is_valid():
            cart = form.save(request.session.session_key)
            return redirect(cart) 
    return render(request, "home.html", {"products": products, "form": form})

def cart(request, cart_id):
    cart = Cart.objects.get(pk=cart_id)
    return render(request, "cart.html", {"cart" : cart})