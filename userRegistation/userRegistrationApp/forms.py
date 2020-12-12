from django import forms
from userRegistrationApp.models import UserProfileDetails

class UserProfileInfoForm(forms.ModelForm):
    user_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserProfileDetails
        fields = ('user_name', 'user_password', 'user_email1', 'user_email2')