from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from product.models import Product
from cart.forms import CartAddProductForm


def homepage(request):
    return render(request, 'main/home_page.html')

def katalog(request):
    return render(request, 'main/katalog.html')

class Search(ListView):
    template_name = 'main/search.html'
    context_object_name = 'product'
    paginate_by = 5

    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        context['cart_product_form'] = CartAddProductForm()
        return context

    def post(self, request, *args, **kwargs):
        cart_product_form = CartAddProductForm(request.POST)
        if cart_product_form.is_valid():
            cart_product_form.save()
            return redirect('hleb')
        return self.get(request, *args, **kwargs)
