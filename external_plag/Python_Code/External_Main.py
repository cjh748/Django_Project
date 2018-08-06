from TextPreprocessing import Pre_Processing
from external_plag.Python_Code.External_Ngram_Matching import all_n_gram_execution


# ===================
# File Pre-Processing
# ===================
def WORDNET_pre_proc(original_corpus, suspicious_corpus):
    pre_processed_files = []
    sus = []
    orig = []
    for text in original_corpus:
        original = Pre_Processing.lower_case(text)
        original = Pre_Processing.remove_punctuation(original)
        original = Pre_Processing.clean_text(original)
        orig.append(original)
    pre_processed_files.append(orig)

    for text in suspicious_corpus:
        suspicious = Pre_Processing.lower_case(text)
        Pre_Processing.remove_punctuation(suspicious)
        Pre_Processing.clean_text(suspicious)
        sus.append(suspicious)
    pre_processed_files.append(sus)
    print("WordNet Pre-Processing Complete")
    return pre_processed_files


def NGRAM_pre_proc(original_corpus, suspicious_corpus):
    pre_processed_files = []
    sus = []
    orig = []
    for text in original_corpus:
        original = Pre_Processing.lower_case(text)
        original = Pre_Processing.remove_punctuation(original)
        original = Pre_Processing.clean_text(original)
        original = Pre_Processing.tokenization(original)
        original = Pre_Processing.remove_stopwords(original)
        original = Pre_Processing.lemmatize_words(original)
        orig.append(original)
    pre_processed_files.append(orig)

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


def TFIDF_pre_proc(original_corpus, suspicious_corpus):
    pre_processed_files = []
    sus = []
    orig = []
    for text in original_corpus:
        original = Pre_Processing.lower_case(text)
        original = Pre_Processing.remove_punctuation(original)
        original = Pre_Processing.clean_text(original)
        original = Pre_Processing.tokenization(original)
        original = Pre_Processing.remove_stopwords(original)
        original = Pre_Processing.lemmatize_words(original)
        orig.append(original)
    pre_processed_files.append(orig)

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


def LCS_pre_proc(original_corpus, suspicious_corpus):
    pre_processed_files = []
    sus = []
    orig = []
    for text in original_corpus:
        original = Pre_Processing.lower_case(text)
        original = Pre_Processing.remove_punctuation(original)
        original = Pre_Processing.clean_text(original)
        orig.append(original)
    pre_processed_files.append(orig)

    for text in suspicious_corpus:
        suspicious = Pre_Processing.lower_case(text)
        suspicious = Pre_Processing.remove_punctuation(suspicious)
        suspicious = Pre_Processing.clean_text(suspicious)
        sus.append(suspicious)
    pre_processed_files.append(sus)
    print("LCS Pre-Processing Complete")
    return pre_processed_files
