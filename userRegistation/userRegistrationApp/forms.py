from django import forms
from userRegistrationApp.models import UserProfileDetails
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileDetails
        fields = ('user_email1', 'user_email2')