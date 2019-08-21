from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from django.contrib.auth import get_user_model
from .user_preferences import MOVIE_PREFERENCES, CHOICES_GENDER, MUSIC_PREFERENCES, AGE_CHOICES, LITERATURE_PREFERENCES

# Create your models here.


class MyUser(AbstractUser):
    about_myself = models.TextField(blank=True)


class UserProfile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='images/')
    age = models.IntegerField(default=25)
    age_for_search = MultiSelectField(r"Preferred age for partner", choices=AGE_CHOICES, default=AGE_CHOICES[1][1])
    gender = models.IntegerField(r"Gender", choices=CHOICES_GENDER, default=CHOICES_GENDER[0][0])
    gender_for_search = MultiSelectField(r"I'm searching for", choices=CHOICES_GENDER, default=CHOICES_GENDER[0][0])
    interests = models.CharField(max_length=50, blank=True)
    create_date = models.DateTimeField('date created', null=True)
    email = models.EmailField()
    movie_preferences = MultiSelectField(choices=MOVIE_PREFERENCES, default=MOVIE_PREFERENCES[0][0])
    literature_preferences = MultiSelectField(choices=LITERATURE_PREFERENCES, default=LITERATURE_PREFERENCES[0][0])
    music_preferences = MultiSelectField(choices=MUSIC_PREFERENCES, default=MUSIC_PREFERENCES[0][0])

    def __str__(self):
        return self.name
