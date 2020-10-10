from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse


class MakeOrder(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = OrderCreateForm
        return render(request, 'orders/order/ncreate.html',
                      {'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        cart = Cart(request)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/order/ncreated.html',
                          {'order': order})
