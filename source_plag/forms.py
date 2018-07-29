from django import forms
from .models import  Original


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class OriginalSelectionForm(forms.Form):
    def __init__(self,corpus,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        #corpus_id = kwargs['corpus_id']

        self.fields['originals'] = forms.ModelChoiceField(queryset = corpus.original_set.all())

    #originals =  forms.ChoiceField()