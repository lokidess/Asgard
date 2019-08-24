from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, UpdateView, FormView
from .models import MyUser
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserProfileForm

# Create your views here.


class HomePageView(ListView):
    model = get_user_model()
    template_name = 'home.html'


class RegistrationUserView(FormView):
    model = get_user_model()
    template_name = 'registration/register_form.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(data=request.POST, files=request.FILES)
        print(form)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return super(RegistrationUserView, self).form_valid(form)


class UpdateUserProfileView(UpdateView):
    model = get_user_model()
    form_class = UserProfileForm
    template_name = 'user_profile.html'
    success_url = reverse_lazy('user_detail')

    def get_object(self, queryset=None):
        return self.request.user


class UserDetailView(ListView):
    model = get_user_model()
    template_name = 'user_detail.html'



