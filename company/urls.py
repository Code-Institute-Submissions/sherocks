from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_company, name="view_company"),
]
