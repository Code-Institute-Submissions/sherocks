from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    template = "profiles/profile.html"
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    context = {
        "orders": orders,
        "form": form,
    }
    return render(request, template, context)
