from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from qa.helper import paginate
from qa.models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)

@require_GET
def get_question(request, pk):
    question = get_object_or_404(Question, id=pk)
    return render(request, '../templates/question.html', {
        'question': question,
        'answers': question.answer_set.all(),
    })

def get_popular(request):
    questions = Question.objects.order_by('-rating')
    page = paginate(request, questions)
    page.paginator.base_url = '/popular/?page='
    return render(request, '../templates/popular.html', {
        'questions': page.object_list,
        'paginator': page.paginator,
        'page': page,
    })

def get_index(request):
    questions = Question.objects.order_by('-added_at')
    page = paginate(request, questions)
    page.paginator.base_url = '/?page='
    return render(request, '../templates/index.html', {
        'questions': page.object_list,
        'paginator': page.paginator,
        'page': page,
    })