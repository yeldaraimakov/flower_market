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
    path('about/', TemplateView.as_view(template_name='flower_market/about.html'), name='about'),
    path('how-to-pay/', TemplateView.as_view(template_name='flower_market/how_to_pay.html'), name='how_to_pay'),

    path('summer/', TemplateView.as_view(template_name='flower_market/summer.html'), name='summer'),
    path('birthday/', TemplateView.as_view(template_name='flower_market/birthday.html'), name='birthday'),
    path('rose/', TemplateView.as_view(template_name='flower_market/rose.html'), name='rose'),
    path('flowers/', TemplateView.as_view(template_name='flower_market/flowers.html'), name='flowers'),
    path('compositions/', TemplateView.as_view(template_name='flower_market/compositions.html'), name='compositions'),

    path('bouquets/tulips/', TemplateView.as_view(template_name='flower_market/tulips.html'), name='tulips'),
    path('bouquets/rose/', TemplateView.as_view(template_name='flower_market/roses.html'), name='roses'),
    path('bouquets/iris/', TemplateView.as_view(template_name='flower_market/iris.html'), name='iris'),
    path('bouquets/lily/', TemplateView.as_view(template_name='flower_market/lily.html'), name='lily'),
    path('bouquets/chrysanthemum/', TemplateView.as_view(template_name='flower_market/chrysanthemum.html'), name='chrysanthemum'),
    path('bouquets/gerber/', TemplateView.as_view(template_name='flower_market/gerber.html'), name='gerber'),
    path('bouquets/alstroemeria/', TemplateView.as_view(template_name='flower_market/alstroemeria.html'), name='alstroemeria'),

]
