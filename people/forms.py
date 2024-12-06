from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomeUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomeUser 
        fields = ['username', 'email', 'password1', 'password2', 'sex']  # Ensure 'username' starts with a lowercase 'u'


class UserLoginForm(AuthenticationForm):
    pass


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomeUser
        fields = ['username', 'email', 'bio', 'sex']
