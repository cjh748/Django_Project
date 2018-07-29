from nltk import ngrams


def ngram_generator(n_value, text):
    split_grams = ngrams(text, n_value)
    joined_grams = []
    for sentence in split_grams:
        joined = ' '.join(sentence)
        joined_grams.append(joined)
    return joined_grams


def similarity_generator(str1, str2, n_gram):
    pairs1 = ngram_generator(n_gram, str1)
    pairs2 = ngram_generator(n_gram, str2)
    intersection = 0
    union = len(pairs1) + len(pairs2)
    for i in range(0, len(pairs1)):
        pair1 = pairs1[i]
        for j in range(0, len(pairs2)):
            pair2 = pairs2[j]
            if pair1 == pair2:
                intersection += 1
                del pairs2[j]
                break
    similarity_score = round(((2.0 * intersection)/union * 100), 1)
    return similarity_score


def single_n_gram_execution(str1, str2, n_gram, original_filename, suspicious_filenames):
    if n_gram == 1:
        n_name = 'unigram'
    elif n_gram == 2:
        n_name = 'bigram'
    elif n_gram == 3:
        n_name = 'trigram'
    elif n_gram == 4:
        n_name = 'quadgram'
    elif n_gram == 5:
        n_name = 'quingram'

    print("===================================================================="
          "=============================")
    print("Execution of " , n_name ," overlap for original file: " ,
          original_filename , " achieved a similarity score of: ")
    print("===================================================================="
          "=============================")

    similarities = []
    for i in range(len(str2)):
        similarity_score = similarity_generator(str1, str2[i], n_gram)
        similarities.append(similarity_score)
        print(similarity_score)

    return similarities


def all_n_gram_execution(str1, str2, original_filename, suspicious_filename):
    retval = []
    for i in range(1, 6):
        retval.append(single_n_gram_execution(str1, str2, i, original_filename, suspicious_filename))
    return retval
