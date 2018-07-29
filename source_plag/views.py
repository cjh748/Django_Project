from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from source_plag.forms import UploadFileForm, OriginalSelectionForm
from .models import Corpus, Original, Suspicious
from source_plag.Python_Code import Source_Main, Source_N_Gram_Matching, Source_TFIDF_gensim, Source_Wordnet_Synsets


def source_plagiarism(request):
    return render(request, 'html/source_plag.html')


class CorpusDetailView(DetailView):
    model = Corpus

    def get_context_data(self, **kwargs):
        context = super(CorpusDetailView, self).get_context_data(**kwargs)
        context['originals_form'] = OriginalSelectionForm(corpus = self.get_object())
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

    success_url = reverse_lazy('list-corpus')


class CreateSuspiciousView(CreateView):
    template_name = 'source_plag/corpus_form.html'
    model = Suspicious
    fields = ['corpus', 'suspicious_file_names', 'suspicious_file']

    success_url = reverse_lazy('list-corpus')


def start_detection(request):
    if request.method == 'POST':
        form = OriginalSelectionForm(data=request.POST)
        if form.is_valid():
            original_obj = form.cleaned_data['originals']
            #corpus_obj = original_obj.corpus
            request.session['step'] = 'pre_process'
            request.session['original_obj'] = original_obj.pk

            return render(request, template_name='source_plag/start_plag.html')
        else:
            return HttpResponse("Invalid values")


def multistep_process(request):
    original_obj = Original.objects.get(pk=request.session['original_obj'])
    corpus_obj = original_obj.corpus
    step = request.GET['step']
    suspicious_data = []
    suspicious_filenames = []
    suspicious_obj = Suspicious.objects.filter(corpus=corpus_obj)
    print(original_obj)
    print(original_obj.display_text_file_orig())
    for sus in suspicious_obj:
        suspicious_filenames.append(sus)
        suspicious_data.append(sus.display_text_file_sus())

    if step == 'pre_process':

        ## FIRST EXTERNAL METHOD
        print("PREPROCESSING.............................")
        pre_process = Source_Main.NGRAM_pre_proc(original_obj.display_text_file_orig(), suspicious_data)
        request.session['pre_process'] = pre_process
        print(original_obj.display_text_file_orig())
        print(pre_process[0])
        # print(pre_process[1][0])
        # print(suspicious_data[0])
        # print(pre_process[1][1])
        # print(suspicious_data[1])
        return JsonResponse({'current_step': step, 'status': 'ok', 'result': pre_process})

    if step == 'ngram':
        print("ngram ----------------------------------------------------")
        pre_process = request.session['pre_process']
        ## SECOND EXTERNAL METHOD
        ngram = Source_N_Gram_Matching.all_n_gram_execution(pre_process[0], pre_process[1], original_obj,
                                                            suspicious_filenames)

        x = render_to_string("source_plag/ngram.html", {'ngrams': ngram})

        return JsonResponse({'current_step': step, 'status': 'ok', 'result': x})

    return JsonResponse({'current_step': 'unspecified', 'status': 'error'})
