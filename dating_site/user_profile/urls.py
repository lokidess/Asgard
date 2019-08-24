from django.urls import path

from .views import HomePageView, RegistrationUserView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register_form/', RegistrationUserView.as_view(), name='register_form'),
]
