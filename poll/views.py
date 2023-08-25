from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in latest_questions])
    return render(request, 'poll/index.html', {
        'latest_questions': latest_questions
    })


# Create your views here

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/details.html', {
        'question': question
    })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST["choice"])

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'poll/details.html', {
            'question': question,
            'error_msg': 'Choice not selected'
        })
    choice.votes += 1
    choice.save()

    return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'poll/result.html', {
        'question': question
    })
