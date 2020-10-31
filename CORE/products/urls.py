from django.urls import path
from . import views
from . views import Home,home,ProductDetail
from cart.views import (add_to_cart ,remove_from_cart,CartView,decreaseCart)

app_name = 'products'
 
urlpatterns = [
    path('p',Home.as_view(),name='home'),
    path('', home, name='home'),
    path('product/<slug>/', ProductDetail.as_view(), name='product'),
    path('cart/', CartView, name='cart-home'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
    path('decrease-cart/<slug>', decreaseCart, name='decrease-cart'),
]
 