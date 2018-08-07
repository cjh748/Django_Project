from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.core.validators import RegexValidator


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, validators=[
        RegexValidator('^(\w+\d+|\d+\w+)+$',
                       message="Please use a combination of letters and numbers in your password.")])
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
