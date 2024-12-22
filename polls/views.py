from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.views import generic
from .forms import ContactForm
from .models import Choice, Question, Contact


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):

        context = {
            "question": question,
            "error_message": "You didn't select a choice.",
        }

        # Redisplay the question voting form.
        return render(request, "polls/detail.html", context)
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def contactForm(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            file = request.FILES.get("file")

            contact = Contact(
                name=name,
                email=email,
                message=message,
                file=file,
            )

            contact.save()  # Save the contact information to the database

            return HttpResponseRedirect(
                reverse("polls:contactSuccess")
            )  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, "polls/contactForm.html", {"form": form})


def contactSuccess(request):
    return render(request, "polls/contactSuccess.html")
