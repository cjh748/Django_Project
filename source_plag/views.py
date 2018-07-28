from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from source_plag.forms import UploadFileForm
from .models import Corpus, Original, Suspicious
from nltk import tokenize


def source_plagiarism(request):
    return render(request, 'html/source_plag.html')


def start_detection(request):
    return render(request, 'source_plag/start_plag.html')


class StartDetectionView(DetailView):
    model = Corpus
    success_url = reverse_lazy('start-detection')


class CorpusDetailView(DetailView):
    model = Corpus

    def get_context_data(self, **kwargs):
        context = super(CorpusDetailView, self).get_context_data(**kwargs)
        context['original_list'] = self.get_object().original_set.all
        context['suspicious_list'] = self.get_object().suspicious_set.all
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
