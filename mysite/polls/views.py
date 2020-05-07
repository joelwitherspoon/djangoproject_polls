from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic


# Create your views here.

# def index(request):
#     """ Index view """
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five questions """
        return Question.objects.order_by('-pub_date')[:5]


# def detail(request, question_id):
#    """Looks at question detail"""
#    question = get_object_or_404(Question, pk=question_id)
#    context = {'question': question}
#    return render(request, 'polls/detail.html', context)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# def results(request, question_id):
#    """ Voting results """
#    question = get_object_or_404(Question, pk=question_id)
#    context = {'question': question}
#    return render(request, 'polls/results.html', context)

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    """ Voting """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        context = {'question': question, 'error_message': 'You didn''t select a choice'}
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
