from django import forms
from .models import MyUser


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = MyUser
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
