from django import forms
from django.core import validators
from accounts.models import User, UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import User as user_auth


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    bot_protect = forms.CharField(required=False, widget=forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)])

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class LogInForm(forms.Form):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
