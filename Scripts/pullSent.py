import pandas
from nltk.corpus import stopwords
import re
from dictCount import dictCount
import numpy as np
# JOY FEAR ANGER SADNESS DISGUST SHAME GUILT

df = pandas.read_csv('ISEAR_FULL.csv', sep=',',)
stop = set(stopwords.words('english'))
joydf = []
feardf = []
angerdf = []
saddf = []
disgustdf = []
shamedf = []
guiltdf = []
removeIndx = []
emotions = ['joy', 'fear', 'anger', 'sadness', 'disgust', 'shame', 'guilt']
for i in range(0,len(df)):
    if(df['SIT'][i][0] != '['):
        sentence = df['SIT'][i]
        sentence = re.sub(r"[^\w\d'\s]+",' ', sentence.lower())
        if((df['EMOT'][i] == 1).any()):
            joydf.append(sentence)
        elif((df['EMOT'][i] == 2).any()):
            feardf.append(sentence)
        elif((df['EMOT'][i] == 3).any()):
            angerdf.append(sentence)
        elif((df['EMOT'][i] == 4).any()):
            saddf.append(sentence)
        elif((df['EMOT'][i] == 5).any()):
            disgustdf.append(sentence)
        elif((df['EMOT'][i] == 6).any()):
            shamedf.append(sentence)
        else:
            guiltdf.append(sentence)

for i in range(0,7):
    fname = emotions[i] + '.txt'
    with open('fname', 'w') as f:
        f.write('\n'.join(shamedf))