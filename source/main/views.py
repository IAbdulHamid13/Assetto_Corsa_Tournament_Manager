from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import ACUserCreationForm

# Create your views here.
def index(request):
    return render(request, 'main/home.html')

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = ACUserCreationForm
    success_url = '/auth/login'

    def form_valid(self, form): # TODO: Alert user of success and email something..
        print("FORM VALID")
        return super().form_valid(form)

    def form_invalid(self, form): # TODO: Indicate failure, maybe reason
        print("FORM INVALID")
        return super().form_invalid(form)

def profile(request):
    # TODO: Get current user
    return render(request, 'main/profile.html')

def schedule(request):
    return render(request, 'main/schedule.html')

def about(request):
    return render(request, 'main/aboutus.html')


