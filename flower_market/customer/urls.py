from django.urls import path
from django.views.generic import TemplateView

from flower_market.customer import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='flower_market/home.html'), name='home'),
    path('order-call/', views.order_call, name='order-call'),
    path('ordering/', views.ordering, name='ordering'),
    path('delivery/', TemplateView.as_view(template_name='flower_market/delivery.html'), name='delivery'),
    path('success-order/', TemplateView.as_view(template_name='flower_market/success_order.html'), name='success_order'),
    path('card/', TemplateView.as_view(template_name='flower_market/card.html'), name='card'),
]
