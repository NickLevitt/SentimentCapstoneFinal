from getSimilarWords import getSimilar

def synScrape():
    #anger, fear, surprise, disgust, happiness and sadness
    anger = [u'angry',u'caustic',u'aggravated',u'furious',u'hostile',u'rage',u'seething',u'ire',u'fury',u'enmity']
    fear = [u'fear',u'concern',u'anxious',u'unease',u'worry',u'panic',u'terror',u'frightening',u'distress',u'trembling']

    allList = getSimilar(anger)
    allList = allList.union(getSimilar(fear))
    pureList = []
    for i in range(0,len(allList)-1):
        pureList.append(str(allList.pop()))

 #   return(pureList)
