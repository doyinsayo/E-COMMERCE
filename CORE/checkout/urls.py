from django.urls import path
from . import views
from . views import checkout

app_name = 'checkout'

urlpatterns = [
     ('checkout/',views.checkout, name="index"),
]
