from django import forms
from .models import Suspicious


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class SuspiciousSelectionForm(forms.Form):
    corpus = forms.IntegerField(widget=forms.HiddenInput);