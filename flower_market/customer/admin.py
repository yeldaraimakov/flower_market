from django.contrib import admin

from .models import OrderCall, Order, OrderItem, OrderDetail

admin.site.register(OrderCall)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderDetail)