import string
import re
import nltk
from collections import Counter
#from Text_Pre_Processing import Norvig_Spell_Check
#WORDS = Counter(Norvig_Spell_Check.words(open('big.txt', encoding='Latin-1').read()))
#from enchant.checker import SpellChecker
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Method 1 - tokenization
def tokenization(text):
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    return tokens


# Method 2 - Remove stopwords
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    filtered_words = []
    for word in text:
        if word not in stop_words:
            filtered_words.append(word)
    filtered_words = [word for word in text if word not in stopwords.words('english')]
    return filtered_words


def clean_text(text):
    text = text.replace('\n', ' ').replace('\r', '').replace(u'\ufeff', '')
    text = re.sub(r'[^\x00-\x7f]', r'', text)
    text = re.sub(' +', ' ', text)
    return text


def append_stopwords(text):
    stop_words = set(stopwords.words('english'))
    filtered_words = []
    for word in text:
        if word in stop_words:
            filtered_words.append(word)
    filtered_words = [word for word in text if word in stopwords.words('english')]
    return filtered_words


def remove_punctuation(text):
    punkt_text = "".join((char for char in text if char not in string.punctuation))
    return punkt_text


def lemmatize_words(text):
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = []
    for word in text:
        lemmatized_sentence.append(lemmatizer.lemmatize(word))
    return lemmatized_sentence


def lower_case(text):
    return text.lower()


# def spell_checker(text):
#     checker = SpellChecker("en_UK", "en_US")
#     checker.set_text(text)
#     for error in checker:
#         suggested_word = error.suggest()[0]
#         error.replace(suggested_word)  # Look here
#     spell_checked = checker.get_text()
#     return spell_checked
#
#
#
# def spell_checker2(text):
#     x = tokenization(text)
#     spell_checked = ''
#     for word in x:
#         word = word.replace(word, Norvig_Spell_Check.correction(word))
#         spell_checked += word + " "
#     return spell_checked


def apply_preproc_internal(suspicious_file, suspicious_filename):
    suspicious_files_filtered = []
    print("====================================================")
    print("Suspicious documentation pre-processing for files: ")
    print("====================================================")
    for i in range(0, len(suspicious_file)):
        print(suspicious_filename[i] + " in progress.....")
        suspicious_filtering = lower_case(suspicious_file[i])
        suspicious_filtering = remove_punctuation(suspicious_filtering)
        #suspicious_filtering = spell_checker(suspicious_filtering)
        suspicious_filtering = tokenization(suspicious_filtering)
        suspicious_filtering = remove_stopwords(suspicious_filtering)
        suspicious_filtering = lemmatize_words(suspicious_filtering)
        suspicious_files_filtered.append(suspicious_filtering)
    print("=================")
    print("Process complete!")
    print("=================")

    return suspicious_files_filtered


def apply_preproc_tests(suspicious_file, suspicious_filename):
    suspicious_files_filtered = []
    print("====================================================")
    print("Suspicious documentation pre-processing for files: ")
    print("====================================================")
    for i in range(0, len(suspicious_file)):
        print(suspicious_filename[i] + " in progress.....")
        suspicious_filtering = lower_case(suspicious_file[i])
        suspicious_filtering = remove_punctuation(suspicious_filtering)
        suspicious_filtering = clean_text(suspicious_filtering)
        # suspicious_filtering = spell_checker(suspicious_filtering)
        suspicious_filtering = tokenization(suspicious_filtering)
        suspicious_filtering = remove_stopwords(suspicious_filtering)
        # suspicious_filtering = lemmatize_words(suspicious_filtering)
        suspicious_files_filtered.append(suspicious_filtering)
    print("=================")
    print("Process complete!")
    print("=================")

    return suspicious_files_filtered

