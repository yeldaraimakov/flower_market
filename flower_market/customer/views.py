import json

from django.contrib import messages
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods

from flower_market.customer.models import OrderCall, Order, OrderDetail, OrderItem


@require_http_methods(["POST"])
def order_call(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')

    messages.success(request, "Спасибо, ваша заявка принята! Мы свяжемся с вами в ближайшее время")

    OrderCall.objects.create(name=name, phone=phone)

    return redirect('home')


@require_http_methods(["POST"])
def ordering(request):
    first_name = request.POST.get('firstname')
    last_name = request.POST.get('lastname')
    phone = request.POST.get('phone')
    delivery_type = request.POST.get('delivery_type')
    json_list = request.POST.get('order_list')
    amount = request.POST.get('order_amount')

    address = ''
    if delivery_type == '1':
        address = request.POST.get('address')

    order_list = json.loads(json_list.replace("'", "\""))

    order_detail = OrderDetail.objects.create(first_name=first_name, last_name=last_name,
                                              phone=phone, delivery_type=delivery_type, address=address)
    order = Order.objects.create(order_detail=order_detail, amount=amount)

    for key in order_list:
        name = order_list.get(key)['name']
        price = order_list.get(key)['price']
        quantity = order_list.get(key)['quantity']

        OrderItem.objects.create(flower_name=name, price=price, quantity=quantity, order=order)

    return redirect('success_order')