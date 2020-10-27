from django.shortcuts import render
from django.contrib import messages

# Create your views here.

# Add to Cart View

def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("products:home")
        else:
            order.orderitems.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("products:home")
    else:
        order = Order.objects.create(
            user=request.user)
        order.orderitems.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("products:home")

# Remove item from cart
def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart = cart_qs[0]
        # Checking the cart quantity
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart_qs.delete()
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user,
            )[0]
            order.orderitems.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect("products:home")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("products:home")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("products:home")        

Django eCommerce tutorial part two django allauth
Posted 11. September 2019. 17 min read.
Cover image
In the last part, we stopped at Adding Items to Cart and Removing items from cart. Now in this part we are going to learn managing every single items in the cart, and in Order . Use Django-allauth to quickly add the Register and Login ability in our Django ecommerce project to the user so they can add the item to the cart.

In this post you may be see some more html part rather than python codes. We are going to use Bootstrap a css framework for rapid design. If you don’t know Bootstrap, then you should check out the amazing tutorial on w3schools or Bootstap official documentation.

Learn Bootstrap is not necessary, but having the knowledge of HTML and CSS will help you make the design look better. For this tutorial I am going to link the GitHub repository so you can download the code and practice.

http://bit.ly/Django-eCommerce-Github-Repo

What we are going to learn in this blog post :
1. **Adding ability to increase and decrease the Product quantity** 2. **Showing the Cart Items in the Cart Page** 3. **Designing our website using Bootstrap** You can skip this part if you don’t like 4. **Adding Registration and Login Feature in our Django Project**
If you missed the previous part of this tutorial series, you can either go back to home page of this blog or use this links to navigate to the corresponding tutorial.
Adding search filters in Django eCommerce website
Real world SAAS application in Django tutorial
Build a SaaS Application in Django 3.0| SaaS Series
Stripe Payment Gateway Integration in Django eCommerce Website
Django eCommerce tutorial part two
So. let’s start the tutorial step by step as we do. Grab a cup of coffee ☕ and start coding.

1. Showing the Cart Items in the Cart Page
In the last part we were able to add items to the cart and in Order but we are able to see that which item we have in the cart and how many quantities we have.

Before we get started make sure you clone the repo from github >>

repo link

For showing the cart items to the corresponding user, we need to create view for the Cart View Page. So, the basic stuff, create a new view in the Cart app, we are calling the view as CartView and we are going to use Function based views for now but letter on we are going to convert this view in Class Based View

CartView Code :

# Cart View
def CartView(request):

    user = request.user

    carts = Cart.objects.filter(user=user)
    orders = Order.objects.filter(user=user, ordered=False)

    if carts.exists():
        order = orders[0]
        return render(request, 'cart/home.html', {"carts": carts, 'order': order})
		
    else:
        messages.warning(request, "You do not have an active order")
        return redirect("core:home")        