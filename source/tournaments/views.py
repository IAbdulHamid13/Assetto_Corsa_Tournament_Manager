# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from tournaments.models import Tournament, Event
from django.views import generic
from django.views.generic.edit import CreateView

class IndexView(generic.ListView):
    # template_name = 'main/tournament_details.html' # TODO
    # context_object_name = 'tournaments_list'

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

