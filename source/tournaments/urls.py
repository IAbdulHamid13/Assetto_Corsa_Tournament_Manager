from django.urls import path
from tournaments import views

app_name = 'tournaments'
urlpatterns = [
    path('', views.IndexView.as_view(), name='all'),
    path('create', views.TournamentCreateView.as_view(), name='create'),
    path('<int:pk>', views.DetailView.as_view(), name='details'),
    path('<int:pk>/register', views.tournament_register, name='tournament_register'),
    path('<int:pk>/events/create', views.EventCreateView.as_view(), name='event_create'),
    path('<int:pk>/events/<int:event_pk>/register', views.event_register, name='event_register')
]