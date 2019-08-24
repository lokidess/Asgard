from django.urls import path

from .views import HomePageView, UpdateUserProfileView, UserDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
	path('my_profile/', UpdateUserProfileView.as_view(), name='update_profile'),
	path('user_detail/', UserDetailView.as_view(), name='user_detail')
]
