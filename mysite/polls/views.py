from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# Create your views here.

class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):

        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(request.POST)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "detail.html", {
            "question": question,
            "error_message": "초이스를 하지 않았습니다."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
