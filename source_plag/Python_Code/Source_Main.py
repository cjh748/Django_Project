import codecs
import os
from source_plag.Python_Code import Source_TFIDF_gensim, Source_N_Gram_Matching, Source_Wordnet_Synsets
from TextPreprocessing import Pre_Processing

# ====================
# DOCUMENT PREPARATION
# ====================
original_filename = "orig_taska.txt"
original_file = open("C:/Users/Chris/Documents/UoB_MSc_Computer_Science/"
                     "MSc_Dissertation/cjh748/Corpus_A/Originals/" + original_filename).read()
suspicious_filenames = os.listdir("C:/Users/Chris/Documents/UoB_MSc_Computer_Science"
                                  "/MSc_Dissertation/cjh748/Corpus_A/Task_A/")
suspicious_files = []
for file in suspicious_filenames:
    with codecs.open("C:/Users/Chris/Documents/UoB_MSc_Computer_Science/"
                     "MSc_Dissertation/cjh748/Corpus_A/Task_A/" + file, "r",
                     encoding='utf-8-sig', errors='ignore') as file_data:
        open_file = file_data.read()
        suspicious_files.append(open_file)


# ===================
# File Pre-Processing
# ===================
# pre_processed_files = Pre_Processing.apply_preproc_source \
#     (original_file, suspicious_files, original_filename, suspicious_filenames)
def WORDNET_pre_proc(original_corpora, suspicious_corpus):
    pre_processed_files = []
    sus = []
    original = Pre_Processing.lower_case(original_corpora)
    Pre_Processing.remove_punctuation(original)
    Pre_Processing.clean_text(original)
    pre_processed_files.append(original)
    for text in suspicious_corpus:
        suspicious = Pre_Processing.lower_case(text)
        Pre_Processing.remove_punctuation(suspicious)
        Pre_Processing.clean_text(suspicious)
        sus.append(suspicious)
    pre_processed_files.append(sus)
    print("WordNet Pre-Processing Complete")
    return pre_processed_files


def NGRAM_pre_proc(original_corpora, suspicious_corpus):
    pre_processed_files = []
    sus = []
    original = Pre_Processing.lower_case(original_corpora)
    original = Pre_Processing.remove_punctuation(original)
    original = Pre_Processing.clean_text(original)
    original = Pre_Processing.tokenization(original)
    original = Pre_Processing.remove_stopwords(original)
    original = Pre_Processing.lemmatize_words(original)
    pre_processed_files.append(original)

    for text in suspicious_corpus:
        suspicious = Pre_Processing.lower_case(text)
        suspicious = Pre_Processing.remove_punctuation(suspicious)
        suspicious = Pre_Processing.clean_text(suspicious)
        suspicious = Pre_Processing.tokenization(suspicious)
        suspicious = Pre_Processing.remove_stopwords(suspicious)
        suspicious = Pre_Processing.lemmatize_words(suspicious)
        sus.append(suspicious)
    pre_processed_files.append(sus)
    print("NGram Overlap Pre-Processing Complete")
    return pre_processed_files


def TFIDF_pre_proc(original_corpora, suspicious_corpus):
    pre_processed_files = []
    sus = []
    original = Pre_Processing.lower_case(original_corpora)
    original = Pre_Processing.remove_punctuation(original)
    original = Pre_Processing.clean_text(original)
    original = Pre_Processing.tokenization(original)
    original = Pre_Processing.remove_stopwords(original)
    original = Pre_Processing.lemmatize_words(original)
    pre_processed_files.append(original)

    for text in suspicious_corpus:
        suspicious = Pre_Processing.lower_case(text)
        suspicious = Pre_Processing.remove_punctuation(suspicious)
        suspicious = Pre_Processing.clean_text(suspicious)
        suspicious = Pre_Processing.tokenization(suspicious)
        suspicious = Pre_Processing.remove_stopwords(suspicious)
        suspicious = Pre_Processing.lemmatize_words(suspicious)
        sus.append(suspicious)
    pre_processed_files.append(sus)
    print("TFIDF Pre-Processing Complete")
    return pre_processed_files


def LCS_pre_proc(original_corpora, suspicious_corpus):
    pre_processed_files = []
    sus = []
    original = Pre_Processing.lower_case(original_corpora)
    original = Pre_Processing.remove_punctuation(original)
    original = Pre_Processing.clean_text(original)
    original = Pre_Processing.tokenization(original)
    original = Pre_Processing.remove_stopwords(original)
    original = Pre_Processing.lemmatize_words(original)
    pre_processed_files.append(original)

    for text in suspicious_corpus:
        suspicious = Pre_Processing.lower_case(text)
        suspicious = Pre_Processing.remove_punctuation(suspicious)
        suspicious = Pre_Processing.clean_text(suspicious)
        suspicious = Pre_Processing.tokenization(suspicious)
        suspicious = Pre_Processing.remove_stopwords(suspicious)
        suspicious = Pre_Processing.lemmatize_words(suspicious)
        sus.append(suspicious)
    pre_processed_files.append(sus)
    print("LCS Pre-Processing Complete")
    return pre_processed_files


TFIDF_files = TFIDF_pre_proc(original_file, suspicious_files)
NGRAM_files = NGRAM_pre_proc(original_file, suspicious_files)
WORDNET_files = WORDNET_pre_proc(original_file, suspicious_files)
LCS_files = LCS_pre_proc(original_file, suspicious_files)

# ========
# WordNet
# ========
Source_Wordnet_Synsets.execute_WORDNET(original_file, original_filename, suspicious_files, suspicious_filenames)

# ===================================================
# Term Frequency - Inverse Document Frequency (TFIDF)
# ===================================================
TFIDF_final = Source_TFIDF_gensim.TFIDF_execution(TFIDF_files, original_filename, suspicious_filenames)

# ==============
# N-Gram Overlap
# ==============

#Source_N_Gram_Matching.all_n_gram_execution(NGRAM_files[0], NGRAM_files[1], original_filename, suspicious_filenames)
