import gensim


def TFIDF_execution(filtered_text, original_filename, suspicious_filenames):
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
    query = tfidf_model[bow_compare]
    cosine_similarity = similarities[query]


    # PRINT PERCENTAGE SIMILARITIES
    suspicious_filenames2 = suspicious_filenames
    print()
    print("TFIDF for original file: " + original_filename)
    print()
    for i in range(0, len(suspicious_files)):
        print(suspicious_filenames2[i] + ":  " + str(round(cosine_similarity[i] * 100, 2)) + "%")
    return cosine_similarity
