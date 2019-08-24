from django.urls import path

from .views import HomePageView, UpdateUserProfileView, UserDetailView, RegistrationUserView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
	path('my_profile/', UpdateUserProfileView.as_view(), name='update_profile'),
	path('user_detail/', UserDetailView.as_view(), name='user_detail'),
    path('register_form/', RegistrationUserView.as_view(), name='register_form'),
]
