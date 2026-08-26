from django.http import HttpResponse
from django.urls import path

def index(request):
    return HttpResponse('Tournament Manager index')

def login(request):
    return HttpResponse('Login page')

def register(request):
    return HttpResponse('Register page')

def profile(request):
    # TODO: Get current user
    return HttpResponse('Profile page')

def schedule(request):
    return HttpResponse('Schedule page')

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('profile', profile, name='profile'),
    path('schedule', schedule, name='schedule')
]