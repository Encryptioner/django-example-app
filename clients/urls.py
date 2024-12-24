from django.urls import path
from .views import client_signup_view, client_login_view

urlpatterns = [
    path("signup/", client_signup_view, name="client_signup"),
    path("login/", client_login_view, name="client_login"),
]
