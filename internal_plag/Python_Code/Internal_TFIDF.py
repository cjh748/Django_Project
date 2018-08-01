import gensim
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')


def TFIDF_execution(filtered_text, suspicious_filenames):
    original_file = filtered_text[0]
    suspicious_files = filtered_text[1]

    # CREATE DICTIONARY
    dictionary = gensim.corpora.Dictionary(suspicious_files)
    all_words = [dictionary.doc2bow(document) for document in suspicious_files]
    dictionary_size = len(dictionary)

    # PERFORM TF-IDF
    tfidf_model = gensim.models.TfidfModel(all_words)
    similarities = gensim.similarities. \
        Similarity(str(dictionary_size), tfidf_model[all_words], dictionary_size)
    bow_compare = dictionary.doc2bow(original_file)
    #print("bow_compare: " + str(bow_compare))
    query = tfidf_model[bow_compare]
    #print("query: " + str(query))
    cosine_similarity = similarities[query]

    # PRINT PERCENTAGE SIMILARITIES
    sim_percentages = []
    for x in cosine_similarity:
        x = round(x * 100, 2)
        sim_percentages.append(x)

    return sim_percentages
