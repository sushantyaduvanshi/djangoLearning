from django import forms
from appTwo.models import userProfile
from django.contrib.auth.models import User

class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']
        labels = {
            'username':'Create Username',
            'email':'Email',
            'password':'Create Password',
        }
        widgets = {
            'password':forms.PasswordInput
        }

class userProfileForm(forms.ModelForm):
    class Meta:
        model = userProfile
        exclude = ['user']
