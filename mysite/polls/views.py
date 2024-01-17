from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Question


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return render(request, "index.html", {"latest_question_list": latest_question_list})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "detail.html", {"question": question})


def results(request, question_id):
    pass


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
