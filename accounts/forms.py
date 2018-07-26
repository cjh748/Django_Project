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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # check and raise error if other user already exists with given email
        is_exists = User.objects.filter(email=email).exists()
        if is_exists:
            raise forms.ValidationError("User already exists with this email")
        return email

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean(self):
        data = self.cleaned_data
        # use your logic for non field errors
        return data


class LogInForm(forms.Form):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
