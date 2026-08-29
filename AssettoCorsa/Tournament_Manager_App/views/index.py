from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render

def index(request):
    return render(request, 'Tournament_Manager_App/home.html')

def login(request):
    return HttpResponse('Login page')

def register(request):
    return HttpResponse('Register page')

def profile(request):
    # TODO: Get current user
    return render(request, 'Tournament_Manager_App/profile.html')

def schedule(request):
    return render(request, 'Tournament_Manager_App/schedule.html')

def about(request):
    return render(request, 'Tournament_Manager_App/aboutus.html')


urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('profile', profile, name='profile'),
    path('schedule', schedule, name='schedule'),
    path('about',about, name='about'),
]