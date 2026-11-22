from django.shortcuts import render
from django.http import HttpResponse

def trial(request):
    info = {'name':'Soham', 'class':'TYBSc', 'college':'MIT'},
    return render(request, 'about.html', info)


