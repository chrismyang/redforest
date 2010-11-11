from django.shortcuts import render_to_response
from django.template import RequestContext


def login(request):
    return render_to_response('Login.html', {}, context_instance=RequestContext(request))