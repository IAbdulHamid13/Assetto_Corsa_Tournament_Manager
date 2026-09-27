from django.db import models
from main.models import User

# Create your models here.
class Event(models.Model):
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE, related_name='events')
    track = models.CharField(max_length=255)
    event_time = models.DateTimeField()
    server = models.OneToOneField('main.Server', on_delete=models.CASCADE, null=True, blank=True)
    available_cars = models.ManyToManyField('main.Car', related_name='events')
 
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    max_participants = models.PositiveIntegerField() # Determined by track with smallest capacity
    participants = models.ManyToManyField(User, related_name='tournaments', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class EventEntry(models.Model):
    """Tracks driver car selections per event"""
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='entries')
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_entries')
    selected_car = models.ForeignKey('main.Car', on_delete=models.SET_NULL, null=True)
    skin = models.CharField(max_length=255, blank=True)