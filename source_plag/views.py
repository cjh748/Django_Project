from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from source_plag.forms import UploadFileForm
from .models import Corpus, Original, Suspicious


def source_plagiarism(request):
    return render(request, 'html/source_plag.html')


class CorpusDetailView(DetailView):
    model = Corpus

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        file =  self.get_object().original_set.all().first().original_file
        context['original_text'] = file.read().decode('utf-8')
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


class CreateOriginalView(CreateView): #DeleteView #UpdateView
    model = Original
    template_name = 'source_plag/corpus_form.html'
    fields = ['corpus', 'original_file_name', 'original_file']

    success_url = reverse_lazy('create-suspicious')


class CreateSuspiciousView(CreateView):
    template_name = 'source_plag/corpus_form.html'
    model = Suspicious
    fields = ['corpus', 'suspicious_file_names', 'suspicious_file']



# def create_corpus(request):
#


# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render_to_response('upload.html', {'form': form})
