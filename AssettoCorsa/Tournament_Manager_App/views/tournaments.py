from django.urls import path
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from Tournament_Manager_App.models import Tournament
from django.views import generic

class IndexView(generic.ListView):
    template_name = '' # TODO
    context_object_name = 'tournaments_list'

    def get_queryset(self):
        return Tournament.objects

class DetailView(generic.DetailView):
    model = Tournament
    template_name = '' # TODO


urlpatterns = [
    path('', IndexView.as_view(), name='all'),
    path('<int:pk>', DetailView.as_view(), name='details'),
]