from django.shortcuts import redirect


def non_logged_in_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:  # Redirect logged-in users
            return redirect("/polls/")
        return view_func(request, *args, **kwargs)

    return wrapper
