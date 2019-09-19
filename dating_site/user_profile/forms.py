from django import forms
from .models import MyUser
from django.contrib.auth import get_user_model
from .user_preferences import MOVIE_PREFERENCES, CHOICES_GENDER, MUSIC_PREFERENCES, AGE_CHOICES, LITERATURE_PREFERENCES
from django.utils.translation import ugettext_lazy as _


class UserRegisterForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput,
                                help_text=_("Enter the same password as above, for verification."))
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

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    

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


