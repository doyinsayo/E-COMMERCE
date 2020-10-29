from django.shortcuts import render
from .models import BillingForm

# Create your views here.

def checkout(request):
    
	# Checkout view
	form = BillingForm
	
	order_qs = Order.objects.filter(user= request.user, ordered=False)
	order_items = order_qs[0].orderitems.all()
	order_total = order_qs[0].get_totals() 
	context = {"form": form, "order_items": order_items, "order_total": order_total}
	# Getting the saved saved_address
	saved_address = BillingAddress.objects.filter(user = request.user)
	if saved_address.exists():
		savedAddress = saved_address.first()
		context = {"form": form, "order_items": order_items, "order_total": order_total, "savedAddress": savedAddress}
	if request.method == "POST":
		saved_address = BillingAddress.objects.filter(user = request.user)
		if saved_address.exists():

			savedAddress = saved_address.first()
			form = BillingForm(request.POST, instance=savedAddress)
			if form.is_valid():
				billingaddress = form.save(commit=False)
				billingaddress.user = request.user
				billingaddress.save()
		else:
			form = BillingForm(request.POST)
			if form.is_valid():
				billingaddress = form.save(commit=False)
				billingaddress.user = request.user
				billingaddress.save()
				
	return render(request, 'checkout/index.html', context)