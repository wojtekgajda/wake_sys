from datetime import datetime

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from wake_sys.models import Reservation, Profile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128, widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(), )


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class DateInput(forms.DateInput):
    input_type = 'date'


class ReservationForm(forms.ModelForm):
    day = forms.DateField(initial=datetime.now().date(), widget=DateInput)

    class Meta:
        model = Reservation
        exclude = ['user']


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['day', 'hour', 'start_slot', 'instructor', 'gear' ]




