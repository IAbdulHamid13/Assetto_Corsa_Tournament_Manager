from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),  
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/register', RegisterView.as_view(), name='register'),
    path('profile', profile, name='profile'),
    path('schedule', schedule, name='schedule'),
    path('about',about, name='about'),
]