from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
<<<<<<< HEAD
from django.template import Context
=======
from telperion.models import User
from django.http import HttpResponse,HttpResponseRedirect

>>>>>>> 75ec7ebbab3e1f34276fc2b018212ea132e18059

def loginpage(request):
    return render_to_response('Login.html', {}, context_instance=RequestContext(request))

def login(request):
<<<<<<< HEAD
    return render_to_response('Login.html', {}, context_instance=RequestContext(request))


def mainpage(request):
    c = Context({
        'college_name': college_name,
        'college_list':["asdf","asdf","fdsa"],
        'question_list':["question 1","question 2"],
    })
=======
    try:
        u = User.objects.get(username=request.POST['username'])
        if u.password == request.POST['password']:
            request.session['uid'] = u.id
            return HttpResponse("Successfully Logged In")
        else:
            return render_to_response('Login.html', {'login': 0}, context_instance=RequestContext(request))
    except User.DoesNotExist:
        return render_to_response('Login.html', {'login': 0}, context_instance=RequestContext(request))
>>>>>>> 75ec7ebbab3e1f34276fc2b018212ea132e18059
