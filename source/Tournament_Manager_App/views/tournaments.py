from django.urls import path
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from Tournament_Manager_App.models import Tournament, Event
from django.views import generic
from django.views.generic.edit import CreateView

class IndexView(generic.ListView):
    template_name = '' # TODO
    context_object_name = 'tournaments_list'

    def get_queryset(self):
        return Tournament.objects # TODO: Get the list of tournaments the user owns

class DetailView(generic.DetailView):
    model = Tournament
    template_name = '' # TODO

class TournamentCreateView(CreateView):
    model = Tournament
    template_name = '' # TODO
    fields = ['name']

class EventCreateView(CreateView):
    model = Event
    template_name = '' # TODO
    fields = ['name']


def tournament_register(request, pk):
    user = None # TODO: Get current user
    tournament = get_object_or_404(Tournament, pk=pk)
    # TODO: Check if tournament full
    # TODO: tournament.participants.append(user)
    return HttpResponse('Registered user for tournament')

def event_register(request, pk, event_pk):
    user = None # TODO: Get current user
    event = get_object_or_404(Event, pk=event_pk)
    # TODO: Create event entry using user and event and chosen car
    return HttpResponse('User selected car for event')

app_name='tournaments'
urlpatterns = [
    path('', IndexView.as_view(), name='all'),
    path('create', TournamentCreateView.as_view(), name='create'),
    path('<int:pk>', DetailView.as_view(), name='details'),
    path('<int:pk>/register', tournament_register, name='tournament_register'),
    path('<int:pk>/events/create', EventCreateView.as_view(), name='event_create'),
    path('<int:pk>/events/<int:event_pk>/register', event_register, name='event_register')
]