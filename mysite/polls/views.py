from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Question


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return render(request, "index.html", {"latest_question_list": latest_question_list})


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("퀘스천이 없어요")
    return render(request, "detail.html", {"question": question})


def results(request, question_id):
    pass


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
