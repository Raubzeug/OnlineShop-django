from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Category, Product
from cart.forms import CartAddProductForm


class IndexPageView(View):
    template_name = 'catalog_app/index.html'

    def get(self, request):
        products = Product.objects.all()
        cart_product_form = CartAddProductForm()
        args = {
            'products': products,
            'cart_product_form': cart_product_form,
        }
        return render(request, template_name=self.template_name, context=args)


class ProductPageView(View):
    template_name = 'catalog_app/product_page.html'

    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        cart_product_form = CartAddProductForm()
        args = {
            'product': product,
            'cart_product_form': cart_product_form,
        }
        return render(request, template_name=self.template_name, context=args)
