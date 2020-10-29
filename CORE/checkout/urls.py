from django.urls import path
from . import views
from . views import checkout,payment

app_name = 'checkout'

urlpatterns = [
    path('checkout/',views.checkout,name="index"),
    path('payment/', payment, name="payment"),
]
