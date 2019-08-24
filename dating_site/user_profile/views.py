from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView
from django.http import HttpResponseRedirect
from .models import UserProfile
from django.urls import reverse_lazy
from .forms import UserRegisterForm

# Create your views here.


class HomePageView(ListView):
    model = UserProfile
    template_name = 'home.html'


class RegistrationUserView(FormView):
    model = UserProfile
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


