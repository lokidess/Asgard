from django import forms
from .models import MyUser
from django.contrib.auth import get_user_model


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = get_user_model()
		fields = [
			'name',
			'avatar',
			'gender',
			'gender_for_search',
			'age',
			'age_for_search',
			'interests',
			'email',
			'movie_preferences',
			'literature_preferences',
			'music_preferences',
		]
