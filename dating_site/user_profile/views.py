from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import UserProfile
from django.urls import reverse_lazy
from .forms import UserProfileForm

# Create your views here.


class HomePageView(ListView):
    model = UserProfile
    template_name = 'home.html'


class CreateUserProfileView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user_profile.html'
    success_url = reverse_lazy('home')
