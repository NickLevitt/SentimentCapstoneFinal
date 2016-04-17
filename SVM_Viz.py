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
from TextClean import textClean
from cleanLunch import cleanLunch
import numpy as np
import os
import re
from nltk.corpus import stopwords
from splitSent import split_into_sentences
from collections import Counter
from radar import *
from scipy.interpolate import spline
import csv


df = pandas.read_csv('ISEAR_FULL.csv', sep=',', )
stories = textClean()
stop = set(stopwords.words('english'))
sentdf = []
Y_labels = []
for i in range(0, len(df)):
    sentence = df['SIT'][i]
    sentence = re.sub(r"[^\w\d'\s]+", ' ', sentence.lower())
    sentence = sentence.split()
    sentence = [word for word in sentence if word not in stop]
    sentence = ' '.join(sentence)
    sentdf.append(sentence)
    Y_labels.append(df['FIELD1'][i])

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                           alpha=1e-3, n_iter=5, random_state=42)), ])
# Trains the model on the entire ISEAR dataset
text_clf = text_clf.fit(sentdf, Y_labels)
parameters = {'vect__ngram_range': [(1, 1), (1, 2)], 'tfidf__use_idf': (True, False), 'clf__alpha': (1e-2, 1e-3)}
tuned_clf = GridSearchCV(text_clf, parameters, n_jobs=1)
tuned_clf = tuned_clf.fit(sentdf, Y_labels)

#Choose a story to visualize

story = stories[17]
# lunches = cleanLunch()
# story = lunches[0]

pred_txt = []
for i in range(0, len(story) / 15):
    pred_txt.append(' '.join(story[i*15:(i+1)*15]))

predicted = tuned_clf.predict(pred_txt)

data = ['JOY','FEAR','ANGER','SADNESS','DISGUST','SHAME','GUILT']
joyvals = []
fearvals = []
angervals = []
sadvals = []
disgustvals = []
shamevals = []
guiltvals = []

inc = len(predicted) / 50
if (inc == 0):
    inc = 1
for i in range(0,50):
    vals = []
    preds = predicted[i*inc:(i+1)*inc]
    vals.append(float(Counter(preds)['joy']) / len(preds))
    joyvals.append(float(Counter(preds)['joy']) / len(preds))
    vals.append(float(Counter(preds)['fear']) / len(preds))
    fearvals.append(float(Counter(preds)['fear']) / len(preds))
    vals.append(float(Counter(preds)['anger']) / len(preds))
    angervals.append(float(Counter(preds)['anger']) / len(preds))
    vals.append(float(Counter(preds)['sadness']) / len(preds))
    sadvals.append(float(Counter(preds)['sadness']) / len(preds))
    vals.append(float(Counter(preds)['disgust']) / len(preds))
    disgustvals.append(float(Counter(preds)['disgust']) / len(preds))
    vals.append(float(Counter(preds)['shame']) / len(preds))
    shamevals.append(float(Counter(preds)['shame']) / len(preds))
    vals.append(float(Counter(preds)['guilt']) / len(preds))
    guiltvals.append(float(Counter(preds)['guilt']) / len(preds))

    # pgx = (len(story) / 50) * i
    # pgy = pgx + (len(story) / 50)
    # if (pgy > len(story)):
    #     pgy = len(story)
    # data = [
    #         ['JOY','FEAR','ANGER','SADNESS','DISGUST','SHAME','GUILT'],
    #         ('Emotion of words x to y', [
    #             vals
    #         ]),
    #     ]
    # name = "fig" + str(i) + ".png"
    # # buildRadar(data, name)

stitle = 'Alice in Wonderland'
# plt.plot(joyvals)
# plt.plot(fearvals)
# plt.plot(angervals)
# plt.plot(sadvals)
# plt.plot(disgustvals)
# plt.plot(shamevals)
# # plt.plot(guiltvals)
# T = np.array(range(0,50))
# xnew = np.linspace(T.min(),T.max(),300)
# joy_smooth = spline(T,joyvals,xnew)
# sad_smooth = spline(T,sadvals,xnew)
# plt.plot(joy_smooth, linewidth = 2)
# plt.plot(sad_smooth, linewidth = 2)
# plt.legend(['JOY','FEAR','ANGER','SADNESS','DISGUST','SHAME','GUILT'], loc='upper left')
# plt.title(stitle + ' Joy & Sad Emotional Analysis')
# plt.show()

data = [[joyvals], [fearvals], [angervals], [sadvals], [disgustvals], [shamevals], [guiltvals]]

with open('StoryData/CatcherInRyeSent.csv', 'wb') as csvfile:
    cwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(0, len(data)):
        cwriter.writerow(data[i])

#data = [['JOY','FEAR','ANGER','SADNESS','DISGUST','SHAME','GUILT'], [joyvals, fearvals, angervals, sadvals, disgustvals, shamevals, guiltvals]]
print("FINISHED")