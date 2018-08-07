import codecs
import os
import csv

import numpy as np
import pandas as pd

from TextPreprocessing import Pre_Processing

filenames = os.listdir(
    "C:/Users/Chris/Documents/UoB_MSc_Computer_Science/MSc_Dissertation/cjh748/scikit-machine-learning/train_test_corpus")
files = []
array_data = []
array_label = []
for file in filenames:
    with codecs.open("C:/Users/Chris/Documents/UoB_MSc_Computer_Science/"
                     "MSc_Dissertation/cjh748/scikit-machine-learning/train_test_corpus/" + file, "r",
                     encoding='utf-8', errors='ignore') as file_data:
        open_file = file_data.read()
        open_file = Pre_Processing.lower_case(open_file)
        open_file = Pre_Processing.remove_punctuation(open_file)
        open_file = Pre_Processing.clean_text(open_file)
        files.append(open_file)

for file in files:
    if 'inheritance' in file:
        array_data.append(file)
        array_label.append('Inheritance (object-oriented programming)')
    elif 'pagerank' in file:
        array_data.append(file)
        array_label.append('PageRank')
    elif 'vector space model' in file:
        array_data.append(file)
        array_label.append('Vector Space Model')
    elif 'bayes' in file:
        array_data.append(file)
        array_label.append('Bayes' + "'" + ' Theorem')
    else:
        array_data.append(file)
        array_label.append('Dynamic programming')

array_label[11] = 'PageRank'
array_label[18] = 'Bayes' + "'" + ' Theorem'
array_label[31] = 'PageRank'
array_label[57] = 'Vector Space Model'

test_array = []
csv_array = []
for i in range(0, len(array_data)):
    test_array.append([array_data[i], array_label[i]])

with open('data.csv', 'w') as target:
    writer = csv.writer(target)
    writer.writerows(zip(test_array))

data = pd.read_csv('data.csv', header=None)
numpy_array = data.as_matrix()

strarr = numpy_array[:, 0]
X = [strarr[i].split(",")[0].replace("[", '').replace("'", '') for i in range(len(strarr))]
Y = [strarr[i].split(",")[1].replace("]", '').replace("'", '') for i in range(len(strarr))]

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.naive_bayes import MultinomialNB

from sklearn.pipeline import Pipeline

text_clf = Pipeline(
    [('vect', CountVectorizer(stop_words='english')), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())])

text_clf = text_clf.fit(X_train, Y_train)
print(text_clf.score(X, Y))

print(X[7])
predicted = text_clf.predict([X[7]])
print(predicted)
np.mean(predicted == Y_test)

import pickle

# pickle_out = open("model.pickle", "wb")
# pickle.dump(text_clf, pickle_out)


pickle_in = open("model.pickle", 'rb')
model = pickle.load(pickle_in)

x = model.predict(["vector space model is super cool"])
y = model.predict(["pagerank blah hello douche"])

print(y)

import wikipedia

print(wikipedia.WikipediaPage(title='Inheritance (object-oriented programming)').summary)
