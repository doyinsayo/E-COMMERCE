from django.urls import path
from . import views
from . views import checkout,payment,charge,OrderView

app_name = 'checkout'

urlpatterns = [
    path('checkout/',views.checkout,name="index"),
    path('payment/', payment, name="payment"),
    path('charge/',views.charge,name="charge"),
    path('my-orders/',OrderView,name="OrderView")
]
