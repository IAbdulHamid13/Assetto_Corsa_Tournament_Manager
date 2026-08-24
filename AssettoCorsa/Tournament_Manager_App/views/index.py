from django.http import HttpResponse
from django.urls import path

def index(request):
    return HttpResponse('Tournament Manager index')

urlpatterns = [
    path('', index, name='index')
]