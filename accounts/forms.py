from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.core.validators import RegexValidator
from django.contrib.auth import authenticate


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=15, validators=[
        RegexValidator('^(\w+\d+|\d+\w+)+$',
                       message="Please use a combination of letters and numbers in your password.")])
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    username = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=50)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    bot_protect = forms.CharField(required=False, widget=forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        email = self.cleaned_data.get('email')
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match")
        is_exists = User.objects.filter(email=email).exists()
        if is_exists:
            raise forms.ValidationError("User already exists with this email")
        return cleaned_data

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'confirm_password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LogInForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

