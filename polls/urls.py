from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    # ex: /polls/
    # name is helpful for: <a href="{% url 'index' %}">index</a>
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # ex: /polls/contact
    path("contact/", views.contact_form, name="contactForm"),
    # ex: /polls/contact/success
    path("contact/success/", views.contact_success, name="contactSuccess"),
    # ex: /polls/api/contact
    path("api/contact/", views.contact_api, name="apiContactForm"),
]
