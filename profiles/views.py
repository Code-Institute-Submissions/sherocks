from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated!")

    template = "profiles/profile.html"
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    reviews = profile.reviewer.all()
    context = {
        "orders": orders,
        "form": form,
        "reviews": reviews,
    }
    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout-success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
