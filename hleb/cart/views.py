from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from product.models import Product

from .cart import Cart
from .forms import CartAddProductForm, AdressForm
from telegram import Bot
from django.conf import settings

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})


def order_show(request):
    cart = Cart(request)

    initial_values = {'adress': 'Самовывоз'}
    form = AdressForm(request.POST or None, initial=initial_values)

    if request.method == 'POST' and form.is_valid():
        phonenumber = form.cleaned_data['phonenumber']
        delivery = form.cleaned_data['delivery']
        adress = form.cleaned_data['adress']
        time_date = form.cleaned_data['time_date']
        email = request.user.email

        order_info = []
        for item in cart.__iter__():
            order_info.append(f"{item['product'].title} ({item['quantity']} шт.)")

        message = f"Новый заказ:\nТелефон: {phonenumber}\n"
        message += f"Почта: {email}\n"
        if delivery:
            message += f"Адрес: {adress}\n"
        else:
            message += "Самовывоз\n"
        message += "Товары: " + "\n ".join(order_info) + "\n"
        message += f"Дата и время: {time_date}"

        # Отправка сообщения через Telegram бота
        bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
        chat_id = settings.TELEGRAM_CHAT_ID
        bot.send_message(chat_id=chat_id, text=message)


    return render(request, 'cart/order.html', {'cart': cart, 'form': form})
