from django.contrib import admin
from . models import BillingAddress,BillingForm

# Register your models here.
admin.site.register(BillingAddress)
admin.site.register(BillingForm)