from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from qa.forms import AskForm, AnswerForm
from qa.helper import paginate
from qa.models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)


def add_ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
        else:
            print(form.is_bound)
    else:
        form = AskForm()
    return render(request, '../templates/qa/ask.html', {
        'form': form,
    })


@require_POST
def add_answer(request):
    form = AnswerForm(request.POST)
    if form.is_valid():
        answer = form.save()
        url = answer.question.get_url()
        return HttpResponseRedirect(url)


@require_GET
def get_question(request, id):
    question = get_object_or_404(Question, id=id)
    form = AnswerForm()
    return render(request, '../templates/qa/question.html', {
        'question': question,
        'answers': question.answer_set.all(),
        'form': form
    })


def get_popular(request):
    questions = Question.objects.order_by('-rating')
    page = paginate(request, questions)
    page.paginator.base_url = '/popular/?page='
    return render(request, '../templates/qa/popular.html', {
        'questions': page.object_list,
        'paginator': page.paginator,
        'page': page,
    })


def get_index(request):
    questions = Question.objects.order_by('-added_at')
    page = paginate(request, questions)
    page.paginator.base_url = '/?page='
    return render(request, '../templates/qa/index.html', {
        'questions': page.object_list,
        'paginator': page.paginator,
        'page': page,
    })
