from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context

def login(request):
    return render_to_response('Login.html', {}, context_instance=RequestContext(request))


def mainpage(request):
    c = Context({
        'college_name': college_name,
        'college_list':["asdf","asdf","fdsa"],
        'question_list':["question 1","question 2"],
    })