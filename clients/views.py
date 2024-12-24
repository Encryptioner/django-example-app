from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import ClientUserSignupForm
from .decorators import non_logged_in_user


@non_logged_in_user
def signup_view(request):
    if request.method == "POST":
        form = ClientUserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("/polls")
    else:
        form = ClientUserSignupForm()
    return render(request, "clients/signup.html", {"form": form})


@non_logged_in_user
def login_view(request):
    if request.user.is_authenticated:  # Redirect logged-in users
        return redirect("/polls/")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("/")  # Redirect to the home page after login
        else:
            return render(
                request, "clients/login.html", {"error": "Invalid email or password"}
            )

    return render(request, "clients/login.html")


def logout_view(request):
    logout(request)  # Logs out the user
    return redirect("/")  # Redirect to home or login page
