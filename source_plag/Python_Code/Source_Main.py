from TextPreprocessing import Pre_Processing


# ===================
# File Pre-Processing
# ===================
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
    pre_processed_files.append(original)

    for text in suspicious_corpus:
        suspicious = Pre_Processing.lower_case(text)
        suspicious = Pre_Processing.remove_punctuation(suspicious)
        suspicious = Pre_Processing.clean_text(suspicious)
        sus.append(suspicious)
    pre_processed_files.append(sus)
    print("LCS Pre-Processing Complete")
    return pre_processed_files
