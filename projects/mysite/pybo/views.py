from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator


def index(req) :
    question_list = Question.objects.order_by('-create_date')

    page = req.GET.get('page', 1)
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = { 'question_list' : page_obj }

    return render(req, 'pybo/question_list.html', context)


def detail(req, question_id) :
    question = get_object_or_404(Question, id = question_id)
    context = { 'question' : question }

    return render(req, 'pybo/question_detail.html', context)


def answer_create(req, question_id):
    question = get_object_or_404(Question, id = question_id)
    if req.method == 'POST':
        form = AnswerForm(req.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id = question_id)
    else:
        form = AnswerForm()
    context = { 'question' : question, 'form' : form }

    return render(req, 'pybo/question_detail.html', context)


def question_create(req):
    if req.method == 'POST':
        form = QuestionForm(req.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()

    context = { 'form': form }
    return render(req, 'pybo/question_form.html', context)


def test(req) :
    return HttpResponse("테스트임")