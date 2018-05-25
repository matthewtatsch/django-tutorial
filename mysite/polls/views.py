"""
polls views
"""

from django.http import HttpResponse

from .models import Question


def index(request):
    """polls index"""

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_test for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    """detail for question"""

    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    """results for question"""

    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    """voting page"""

    return HttpResponse("You're voting on question %s." % question_id)
