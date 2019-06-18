from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    n = 'Arslan'
    return render(request, 'blog/index.html', context={'name':n})
