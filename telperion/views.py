# Create your views here.
from django.template import Context

def mainpage(request):
    c = Context({
        'college_name': college_name,
        'college_list':["asdf","asdf","fdsa"],
        'question_list':["question 1","question 2"],
    })