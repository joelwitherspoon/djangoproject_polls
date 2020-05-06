from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


# Create your views here.

def index(request):
    """ Index view """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """Looks at question detail"""
    return HttpResponse("You're looking at question %s" % question_id)


def results(request, question_id):
    """ Voting results """
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    """ Voting """
    return HttpResponse("You're voting on question %s." % question_id)
