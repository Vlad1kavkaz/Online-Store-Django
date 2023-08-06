from django.shortcuts import render
from .models import Product
from cart.forms import CartAddProductForm

# Create your views here.

def hleb(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request, 'product/hleb.html', {'product': product,
                                                 'cart_product_form': cart_product_form})

def mangal(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()

    return render(request, 'product/mangal.html', {'product': product,
                                                 'cart_product_form': cart_product_form})

def cake(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()

    return render(request, 'product/cake.html', {'product': product,
                                                 'cart_product_form': cart_product_form})

def meat(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()

    return render(request, 'product/meat.html', {'product': product,
                                                 'cart_product_form': cart_product_form})

def vegetable(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()

    return render(request, 'product/vegetable.html', {'product': product,
                                                 'cart_product_form': cart_product_form})

def meatin(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()

    return render(request, 'product/meatin.html',{'product': product,
                                                 'cart_product_form': cart_product_form})

def bird(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()

    return render(request, 'product/bird.html', {'product': product,
                                                 'cart_product_form': cart_product_form})

def fish(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()

    return render(request, 'product/fish.html',{'product': product,
                                                 'cart_product_form': cart_product_form})

def pot(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()

    return render(request, 'product/pot.html',{'product': product,
                                                 'cart_product_form': cart_product_form})

def salad(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()

    return render(request, 'product/salad.html',{'product': product,
                                                 'cart_product_form': cart_product_form})

def croissant(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()

    return render(request, 'product/croissant.html',{'product': product,
                                                 'cart_product_form': cart_product_form})

def poppy(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()

    return render(request, 'product/poppy.html',{'product': product,
                                                 'cart_product_form': cart_product_form})

def hotcakes(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()

    return render(request, 'product/hotcakes.html',{'product': product,
                                                 'cart_product_form': cart_product_form})

def dumplings(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()

    return render(request, 'product/dumplings.html',{'product': product,
                                                 'cart_product_form': cart_product_form})

def milk(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()

    return render(request, 'product/milk.html',{'product': product,
                                                 'cart_product_form': cart_product_form})

def honey(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()

    return render(request, 'product/honey.html',{'product': product,
                                                 'cart_product_form': cart_product_form})

def hotdrink(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()

    return render(request, 'product/hotdrinks.html',{'product': product,
                                                 'cart_product_form': cart_product_form})
