from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.views.decorators.csrf import csrf_exempt

from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from source_plag.forms import UploadFileForm, OriginalSelectionForm
from .models import Corpus, Original, Suspicious
from source_plag.Python_Code import Source_Main, Source_N_Gram_Matching, Source_TFIDF_gensim, Source_Wordnet_Synsets, \
    Source_LCS_Substring, Source_LCS_Subsequence


class CorpusDetailView(DetailView):
    model = Corpus

    def get_context_data(self, **kwargs):
        context = super(CorpusDetailView, self).get_context_data(**kwargs)
        context['originals_form'] = OriginalSelectionForm(corpus=self.get_object())
        context['suspicious_files'] = self.get_object().suspicious_set.order_by('id')
        return context

    def get_object(self, queryset=None):
        obj = super(CorpusDetailView, self).get_object(queryset);
        if obj.user != self.request.user:
            raise Http404

        return obj

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


@csrf_exempt
def delete_original(request):
    if request.method == 'POST':
        try:
            pk = int(request.POST.get('pk', -1))
            print(pk, request.user)
            obj = Original.objects.get(corpus__user=request.user, pk=pk)
            obj.delete()
            return JsonResponse({'status': 'ok'})
        except ValueError:
            import traceback
            traceback.print_exc()
            raise Http404
        except Original.DoesNotExist:
            import traceback
            traceback.print_exc()
            raise Http404


@csrf_exempt
def delete_suspicious(request):
    if request.method == 'POST':
        try:
            pk = int(request.POST.get('pk', -1))
            print(pk, request.user)
            obj = Suspicious.objects.get(corpus__user=request.user, pk=pk)
            obj.delete()
            return JsonResponse({'status': 'ok'})
        except ValueError:
            import traceback
            traceback.print_exc()
            raise Http404
        except Suspicious.DoesNotExist:
            import traceback
            traceback.print_exc()
            raise Http404


def start_detection(request):
    if request.method == 'POST':
        form = OriginalSelectionForm(data=request.POST)
        if form.is_valid():
            original_obj = form.cleaned_data['originals']
            request.session['step'] = 'pre_process'
            request.session['original_obj'] = original_obj.pk

            return render(request, template_name='source_plag/start_plag.html')
        else:
            return HttpResponse("Invalid values")

    return HttpResponse("We are supposed to recieve a post")


def multistep_process(request):
    original_obj = Original.objects.get(pk=request.session['original_obj'])
    corpus_obj = original_obj.corpus
    step = request.GET['step']
    suspicious_data = []
    suspicious_filenames = []
    suspicious_obj = Suspicious.objects.filter(corpus=corpus_obj)
    for sus in suspicious_obj:
        suspicious_filenames.append(sus)
        suspicious_data.append(sus.display_text_file_sus())

    if step == 'pre_process':
        pre_process = Source_Main.NGRAM_pre_proc(original_obj.display_text_file_orig(), suspicious_data)
        request.session['pre_process'] = pre_process
        return JsonResponse({'current_step': step, 'status': 'ok', 'result': pre_process})

    if step == 'ngram':
        pre_process = request.session['pre_process']
        ngram = Source_N_Gram_Matching.all_n_gram_execution(pre_process[0], pre_process[1])
        ngram2 = []
        for i, s in enumerate(suspicious_filenames):
            slist = []
            for row in ngram:
                slist.append(row[i])
            ngram2.append([s, slist])
        ngram_result = render_to_string("source_plag/ngram.html", {'ngrams': ngram2})
        return JsonResponse({'current_step': step, 'status': 'ok', 'result': ngram_result})

    if step == 'pre_process_tfidf':
        pre_process_tfidf = Source_Main.TFIDF_pre_proc(original_obj.display_text_file_orig(), suspicious_data)
        request.session['pre_process_tfidf'] = pre_process_tfidf

        return JsonResponse({'current_step': step, 'status': 'ok', 'pre_process_tfidf': pre_process_tfidf})

    if step == 'tfidf':
        pre_process_tfidf = request.session['pre_process_tfidf']
        tfidf = Source_TFIDF_gensim.TFIDF_execution(pre_process_tfidf)
        tlist = []
        for i in range(0, len(suspicious_filenames)):
            tlist.append([suspicious_filenames[i], tfidf[i]])

        tfidf_result = render_to_string("source_plag/tfidf.html", {"tfidfs": tlist})
        return JsonResponse({'current_step': step, 'status': 'ok', 'tfidf_result': tfidf_result})

    if step == 'pre_process_wordnet':
        pre_process_wordnet = Source_Main.WORDNET_pre_proc(original_obj.display_text_file_orig(), suspicious_data)
        request.session['pre_process_wordnet'] = pre_process_wordnet
        return JsonResponse({'current_step': step, 'status': 'ok', 'pre_process_wordnet': pre_process_wordnet})

    if step == 'wordnet':
        pre_process_wordnet = request.session['pre_process_wordnet']
        wordnet = Source_Wordnet_Synsets.execute_WORDNET(pre_process_wordnet[0], pre_process_wordnet[1])
        wlist = []
        for i in range(0, len(suspicious_filenames)):
            wlist.append([suspicious_filenames[i], wordnet[i]])

        wordnet_result = render_to_string("source_plag/wordnet.html", {"wordnets": wlist})
        return JsonResponse({'current_step': step, 'status': 'ok', 'wordnet_result': wordnet_result})

    if step == 'pre_process_lcs':
        pre_process_lcs = Source_Main.LCS_pre_proc(original_obj.display_text_file_orig(), suspicious_data)
        request.session['pre_process_lcs'] = pre_process_lcs
        return JsonResponse({'current_step': step, 'status': 'ok', 'pre_process_lcs': pre_process_lcs})

    if step == 'lcs':
        pre_process_lcs = request.session['pre_process_lcs']
        lcs_list = []
        for i in range(0, len(suspicious_filenames)):
            lcs_list.append([suspicious_filenames[i],
                             Source_LCS_Substring.Longest_Common_Substring(pre_process_lcs[0], pre_process_lcs[1][i]),
                             Source_LCS_Subsequence.Longest_Common_Subsequence(pre_process_lcs[0],
                                                                               pre_process_lcs[1][i])])
        lcs_result = render_to_string("source_plag/lcs.html", {"lcss": lcs_list})
        return JsonResponse({'current_step': step, 'status': 'ok', 'lcs_result': lcs_result})

    return JsonResponse({'current_step': 'unspecified', 'status': 'error'})
