from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.grid_search import GridSearchCV
from sklearn import metrics
from sklearn import cross_validation
import pandas
from nltk.corpus import stopwords
import re
from dictCount import dictCount
import numpy as np

df = pandas.read_csv('ISEAR_FULL.csv', sep=',', )
stop = set(stopwords.words('english'))
sentdf = []
Y_labels = []
for i in range(0, len(df)):
    sentence = df['SIT'][i]
    sentence = re.sub(r"[^\w\d'\s]+", ' ', sentence.lower())
    sentence = sentence.split()
    # sentence = [word for word in sentence if word not in stop]
    sentence = ' '.join(sentence)
    sentdf.append(sentence)
    Y_labels.append(df['FIELD1'][i])

# count_vect = CountVectorizer()
# X_train_counts = count_vect.fit_transform(X_train)
# tfidf_transformer = TfidfTransformer()
# X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                           alpha=1e-3, n_iter=5, random_state=42)), ])

# Code for 10-fold cross validation testing
scores1 = cross_validation.cross_val_score(text_clf, sentdf, Y_labels, cv=10)

# Now tuning the SVM
parameters = {'vect__ngram_range': [(1, 1), (1, 2)], 'tfidf__use_idf': (True, False), 'clf__alpha': (1e-2, 1e-3)}
tuned_clf = GridSearchCV(text_clf, parameters, n_jobs=1)

scores2 = cross_validation.cross_val_score(tuned_clf, sentdf, Y_labels, cv=10)

print("Finished with average accuracies of: %0.2f (+/- %0.2f) for non-tuned and %0.2f (+/- %0.2f) for tuned"
      % (scores1.mean(), scores1.std() * 2, scores2.mean(), scores2.std() * 2))
