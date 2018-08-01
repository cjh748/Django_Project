from TextPreprocessing import Pre_Processing


# ===================
# File Pre-Processing
# ===================


def WORDNET_pre_proc(suspicious_corpus):
    pre_processed_files = []
    for text in suspicious_corpus:
        suspicious = Pre_Processing.lower_case(text)
        Pre_Processing.remove_punctuation(suspicious)
        Pre_Processing.clean_text(suspicious)
        pre_processed_files.append(suspicious)
    print("WordNet Pre-Processing Complete")
    return pre_processed_files


def NGRAM_pre_proc(suspicious_corpus):
    pre_processed_files = []
    for text in suspicious_corpus:
        suspicious = Pre_Processing.lower_case(text)
        suspicious = Pre_Processing.remove_punctuation(suspicious)
        suspicious = Pre_Processing.clean_text(suspicious)
        suspicious = Pre_Processing.tokenization(suspicious)
        suspicious = Pre_Processing.remove_stopwords(suspicious)
        suspicious = Pre_Processing.lemmatize_words(suspicious)
        pre_processed_files.append(suspicious)
    print("NGram Overlap Pre-Processing Complete")
    return pre_processed_files


def TFIDF_pre_proc(suspicious_corpus):
    pre_processed_files = []
    for text in suspicious_corpus:
        suspicious = Pre_Processing.lower_case(text)
        suspicious = Pre_Processing.remove_punctuation(suspicious)
        suspicious = Pre_Processing.clean_text(suspicious)
        suspicious = Pre_Processing.tokenization(suspicious)
        suspicious = Pre_Processing.remove_stopwords(suspicious)
        suspicious = Pre_Processing.lemmatize_words(suspicious)
        pre_processed_files.append(suspicious)
    print("TFIDF Pre-Processing Complete")
    return pre_processed_files


def LCS_pre_proc(suspicious_corpus):
    pre_processed_files = []
    for text in suspicious_corpus:
        suspicious = Pre_Processing.lower_case(text)
        suspicious = Pre_Processing.remove_punctuation(suspicious)
        suspicious = Pre_Processing.clean_text(suspicious)
        pre_processed_files.append(suspicious)
    print("LCS Pre-Processing Complete")
    return pre_processed_files
