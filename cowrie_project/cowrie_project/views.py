from django.http import HttpResponse
from django.shortcuts import render

def homepage_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')
