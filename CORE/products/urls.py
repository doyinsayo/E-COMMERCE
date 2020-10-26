from django.urls import path
from . import views
from . views import home

app_name = 'products'
 
urlpatterns = [
    path('',views.home,name='home')
]
 