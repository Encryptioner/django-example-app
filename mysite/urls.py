"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

from debug_toolbar.toolbar import debug_toolbar_urls

admin.site.site_header = "Django Example App"


def home_view(request):
    if request.user.is_authenticated:
        return redirect("/polls/")
    return redirect("/clients/login/")


urlpatterns = (
    [
        path("", home_view, name="home"),
        path("admin/", admin.site.urls),
        path("clients/", include("clients.urls")),
        path("polls/", include("polls.urls")),
    ]
    + debug_toolbar_urls()
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
