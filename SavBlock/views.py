from django.shortcuts import render
from django.http import HttpResponse

'''
def post_list(request):
    return render(request, 'templates/home.html', {})
'''


def index(home_view):
    return render(home_view, 'home-1.html', {})

    '''
    template_name = "home-1.html"
    return HttpResponse("Sav Block index.")
    '''


def list_tribes(request):
    return HttpResponse('Steven Nodalo')
