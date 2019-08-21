from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import MyUser
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .forms import UserProfileForm

# Create your views here.


class HomePageView(ListView):
    model = get_user_model()
    template_name = 'home.html'


class CreateUserProfileView(CreateView):
    model = get_user_model()
    form_class = UserProfileForm
    template_name = 'user_profile.html'
    success_url = reverse_lazy('home')
