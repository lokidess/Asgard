from django.urls import path

from .views import HomePageView, CreateUserProfileView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
	path('new_profile/', CreateUserProfileView.as_view(), name='add_profile'),
]
