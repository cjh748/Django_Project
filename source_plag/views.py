import string

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from source_plag.forms import UploadFileForm, OriginalSelectionForm
from .models import Corpus, Original, Suspicious
from source_plag.Python_Code import Source_Main, Source_N_Gram_Matching, Source_TFIDF_gensim, Source_Wordnet_Synsets


def source_plagiarism(request):
    return render(request, 'html/source_plag.html')


#def start_detection(request):
#    return render(request, 'source_plag/start_plag.html')


#class StartDetectionView(DetailView):
#    model = Corpus
#    success_url = reverse_lazy('start-detection')


class CorpusDetailView(DetailView):
    model = Corpus

    def get_context_data(self, **kwargs):
        context = super(CorpusDetailView, self).get_context_data(**kwargs)
        context['original_list'] = self.get_object().original_set.all
        context['suspicious_list'] = self.get_object().suspicious_set.all
        context['originals_form'] = OriginalSelectionForm(corpus = self.get_object())
        return context


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     orig_file = self.get_object().original_set.all
    #     sus_file = self.get_object().suspicious_set.all
    #     context['original_file'] = orig_file
    #     context['suspicious_file'] = sus_file
    #     return context


class TextPreProcessing(DetailView):
    model = Corpus

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orig_file = self.get_object().original_set.all
        sus_file = self.get_object().suspicious_set.all
        context['original_file'] = orig_file
        context['suspicious_file'] = sus_file
        return context


class CorpusListView(ListView):
    model = Corpus

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class CorpusCreateView(CreateView):
    model = Corpus
    fields = ['corpus_name']

    success_url = reverse_lazy('list-corpus')

    def form_valid(self, form):
        corpus = form.save(False)
        corpus.user_id = self.request.user.id
        corpus.save()
        return HttpResponseRedirect(self.success_url)


class CreateOriginalView(CreateView):  # DeleteView #UpdateView
    model = Original
    template_name = 'source_plag/corpus_form.html'
    fields = ['corpus', 'original_file_name', 'original_file']

    success_url = reverse_lazy('create-suspicious')


class CreateSuspiciousView(CreateView):
    template_name = 'source_plag/corpus_form.html'
    model = Suspicious
    fields = ['corpus', 'suspicious_file_names', 'suspicious_file']

    success_url = reverse_lazy('show-corpus')


def start_detection(request, corpus_name):
    corpus_obj = Corpus.objects.get(corpus_name=corpus_name)
    original_obj = Original.objects.filter(corpus=corpus_obj)
    original_data = []
    original_filenames = []
    for orig in original_obj:
        print(orig)
        original_filenames.append(orig)
        original_data.append(orig.display_text_file_orig())

    suspicious_data = []
    suspicious_filenames = []
    suspicious_obj = Suspicious.objects.filter(corpus=corpus_obj)
    for sus in suspicious_obj:
        print(sus.display_text_file_sus())
        suspicious_filenames.append(sus)
        suspicious_data.append(sus.display_text_file_sus())

    ## FIRST EXTERNAL METHOD
    pre_process = Source_Main.NGRAM_pre_proc(original_data[0], suspicious_data)

    ## SECOND EXTERNAL METHOD
    ngram = Source_N_Gram_Matching.all_n_gram_execution(pre_process[0], pre_process[1], original_filenames, suspicious_filenames)

    return render(request, template_name='source_plag/start_plag.html', context={'pre_process': pre_process})


def remove_punctuation(text):
    punkt_text = "".join((char for char in text if char not in string.punctuation))
    return punkt_text