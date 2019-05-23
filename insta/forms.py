from django import forms
from .models import Image, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'post_date', 'liker','profile_photo']



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']