"""
polls views
"""

from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse

from .models import Question


def index(request):
    """polls index

    Displays the five most recently published questions.
    """

    latest_question_list = get_list_or_404(Question.objects.order_by('-pub_date')[:5])
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    """detail for question"""

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """results for question"""

    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    """voting page"""

    return HttpResponse("You're voting on question %s." % question_id)
