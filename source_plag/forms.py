from django import forms
from .models import  Original


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class OriginalSelectionForm(forms.Form):
    def __init__(self,corpus = None,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        if corpus:
            self.fields['originals'] = forms.ModelChoiceField(queryset = corpus.original_set.all())
        else:
            self.fields['originals'] = forms.ModelChoiceField(queryset = Original.objects.all())