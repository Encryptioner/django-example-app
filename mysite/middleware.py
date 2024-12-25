from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User


class RedirectBasedOnUserTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Check if the user is an admin user
            if isinstance(request.user, User):  # Default admin user
                # Redirect admin users visiting /, /clients, or /polls
                if request.path.startswith("/") and not request.path.startswith(
                    "/admin"
                ):
                    return redirect(reverse("admin:login"))

            # Check if the user is a client-side user
            else:  # Assume client user if not admin
                # Redirect client users visiting /admin
                if request.path.startswith("/admin"):
                    return redirect(reverse("polls:index"))

        return self.get_response(request)
