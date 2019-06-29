from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'home.html', {'fruit':'apple'})

def about(request):
    return HttpResponse('about')

def count(request):
    name = request.GET['fullname']
    return render(request, 'count.html', {'fullname': name})