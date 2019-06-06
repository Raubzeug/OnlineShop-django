from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from catalog_app.models import Product
from .cart import Cart
from .forms import CartAddProductForm


class CartClear(View):
    def get(self, request):
        cart = Cart(request)
        cart.clear()
        return redirect('cart:cart_detail')


class CartAdd(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
        return redirect('cart:cart_detail')


class CartRemove(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')


class CartDetail(View):
    template_name = 'cart/detail.html'

    def get(self, request):
        cart = Cart(request)
        return render(request, template_name=self.template_name, context={'cart': cart})