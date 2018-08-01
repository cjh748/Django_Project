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


def single_n_gram_execution(str1, str2, n_gram):
    similarities = similarity_generator(str1, str2, n_gram)
    return similarities


