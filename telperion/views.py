from django.shortcuts import render_to_response
from django.template import RequestContext
from telperion.models import User
from django.contrib.auth.models import User as OldUser
from django.http import HttpResponse



def loginpage(request):
    return render_to_response('Login.html', {}, context_instance=RequestContext(request))

def login(request):
    try:
        u = OldUser.objects.get(username=request.POST['username'])
        if u.check_password(request.POST['password']):
            request.session['uid'] = u.id
            return HttpResponse("Successfully Logged In")
        else:
            return render_to_response('Login.html', {'login': 0}, context_instance=RequestContext(request))
    except User.DoesNotExist:
        return render_to_response('Login.html', {'login': 0}, context_instance=RequestContext(request))

def create_user(request):
    u = OldUser(username=request.POST['username_new'])
    u.set_password(request.POST['password_new'])
    u.save()
    completeuser = User(user=u)
    completeuser.save()
    request.session['uid'] = u.id
    return HttpResponse('You made a new username. DOOP!')