from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn


####### SOURCE: https://nlpforhackers.io/wordnet-sentence-similarity/

def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'

    if tag.startswith('V'):
        return 'v'

    if tag.startswith('J'):
        return 'a'

    if tag.startswith('R'):
        return 'r'

    return None


def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None

    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None


def sentence_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))

    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]

    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]

    score, count = 0.0, 0

    # For each word in the first sentence
    for synset in synsets1:
        # Get the similarity value of the most similar word in the other sentence
        best_score = [synset.path_similarity(ss) for ss in synsets2]

        best_score = [x for x in best_score if x is not None]

        # Check that the similarity could have been computed
        if best_score:
            best_score = max(best_score)
            score += best_score
            count += 1

    # Average the values
    if count != 0:
        score /= count
    return score


def symmetric_sentence_similarity(sentence1, sentence2):
    """ compute the symmetric sentence similarity using Wordnet """
    return (sentence_similarity(sentence1, sentence2) + sentence_similarity(sentence2, sentence1)) / 2


def execute_WORDNET(suspicious_corpus, j):
    sym_similarities = []
    for i in range(0, len(suspicious_corpus)):
        sym_similarities.append(
            round(symmetric_sentence_similarity(suspicious_corpus[i], suspicious_corpus[j]) * 100, 2))

    return sym_similarities
