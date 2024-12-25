from django.shortcuts import redirect
from django.urls import reverse


class LoginRequiredPollsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Apply @login_required only to the polls app views
        if request.path.startswith("/polls/") and not request.user.is_authenticated:
            return redirect(
                reverse("clients:login")
            )  # Redirect to login page if not authenticated
        return self.get_response(request)
