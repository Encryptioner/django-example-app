from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import ClientUserSignupForm


def client_signup_view(request):
    if request.method == "POST":
        form = ClientUserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("/")
    else:
        form = ClientUserSignupForm()
    return render(request, "clients/signup.html", {"form": form})


def client_login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("/")
        else:
            return render(
                request, "clients/login.html", {"error": "Invalid credentials"}
            )
    return render(request, "clients/login.html")
