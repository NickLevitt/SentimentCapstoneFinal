from TextClean import textClean
from dictCount import dictCount
import numpy as np
import os
import re
from nltk.corpus import wordnet as wn
from collections import Counter
from nltk.corpus import stopwords
import matplotlib.pyplot as plt


allStories = textClean()
for k in range(0,len(allStories)-1):
    story = allStories[k]
    happy = [line.rstrip('\n') for line in open('Stories/emotions/happy.txt')]
    neg = [line.rstrip('\n') for line in open('Stories/emotions/negative.txt')]

    #allEmotion = happy+neg

    totHap = []
    totNeg = []
    totSplit = 26
    split = len(story) / totSplit

    for i in range(0,totSplit-1):
        textChunk = dictCount(story[split*i:split*(i+1)])
        hCount = 0.0
        nCount = 0.0
        for j in range(0, len(happy)):
            hCount += textChunk[happy[j]]

        for j in range(0,len(neg)):
            nCount += textChunk[neg[j]]

        totHap.append(hCount)
        totNeg.append(nCount)

    print ("Number of Happy Words: " + str(totHap))
    print ("Number of Negative Words: " + str(totNeg))
    plt.plot(totHap)
    plt.plot(totNeg)
    plt.savefig(story[0] + "Positive v Happy")
    plt.clf()