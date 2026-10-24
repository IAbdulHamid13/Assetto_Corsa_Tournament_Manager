from django import forms
from django.urls import reverse_lazy
from .models import User
from django.contrib.auth.forms import UserCreationForm

class ACUserCreationForm(UserCreationForm):
    success_page = reverse_lazy('/')
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']