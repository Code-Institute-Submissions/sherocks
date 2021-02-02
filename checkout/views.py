from django.shortcuts import render, redirect, reverse

from .forms import OrderForm


# Create your views here.
def checkout(request):
    bag = request.session.get("bag", {})
    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51I8lsLKHt86mmkjf5iG4QehVRq5sSC9jfuwW8oEkZTZWufZkOWIxcuNLHi0VOs1VQJGWneeYzsOmHprtwiZJA57800SEvLEWdL",
        "client_secret": "test client secret"
    }
    return render(request, template, context)
