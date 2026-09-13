from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Create your views here.
def index(request):
    return render(request, 'main/home.html')

def login(request):
    return HttpResponse('Login page')

def register(request):
    return HttpResponse('Register page')

def profile(request):
    # TODO: Get current user
    return render(request, 'main/profile.html')

def schedule(request):
    return render(request, 'main/schedule.html')

def about(request):
    return render(request, 'main/aboutus.html')


