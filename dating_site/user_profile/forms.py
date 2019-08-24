from django import forms
from .models import MyUser
from django.contrib.auth import get_user_model
from .user_preferences import MOVIE_PREFERENCES, CHOICES_GENDER, MUSIC_PREFERENCES, AGE_CHOICES, LITERATURE_PREFERENCES


class UserRegisterForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=CHOICES_GENDER)
    gender_for_search = forms.ChoiceField(choices=CHOICES_GENDER)
    age_for_search = forms.ChoiceField(choices=AGE_CHOICES)
    movie_preferences = forms.ChoiceField(choices=MOVIE_PREFERENCES)
    literature_preferences = forms.ChoiceField(choices=LITERATURE_PREFERENCES)
    music_preferences = forms.ChoiceField(choices=MUSIC_PREFERENCES)

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

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'interests': forms.Textarea(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

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


