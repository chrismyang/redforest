from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponse



def loginpage(request):
    return render_to_response('Login.html', {}, context_instance=RequestContext(request))

def login(request):
    try:
        u = User.objects.get(username=request.POST['username'])
        if u.check_password(request.POST['password']):
            request.session['uid'] = u.id
            return HttpResponse("Successfully Logged In")
        else:
            return render_to_response('Login.html', {'login': 0}, context_instance=RequestContext(request))
    except User.DoesNotExist:
        return render_to_response('Login.html', {'login': 0}, context_instance=RequestContext(request))
