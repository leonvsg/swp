from django.http import HttpResponse, Http404
from django.shortcuts import render

from qa.models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)

def get_question(request, id):
    try:
       question = Question.objects.get(id=id)
    except:
        Http404
    return render(request, question, "/templates/question.html")
