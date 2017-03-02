import pandas
from nltk.corpus import stopwords
import re
from dictCount import dictCount
import numpy as np
# JOY FEAR ANGER SADNESS DISGUST SHAME GUILT

def emotCount(df):
    emotString = ''

    for i in range(0,len(df)):
        emotString = emotString + ' ' + str(df[i]['SIT'].str.cat())

    cleanEmot = re.sub(r"[^\w\d'\s]+",' ', emotString.lower())
    cleanEmot = cleanEmot.split()
    emotCount = dictCount(cleanEmot)
    return(emotCount)


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

for i in range(0,len(df)):
    if(df['SIT'][i][0] != '['):
        if((df.loc[[i]]['EMOT'] == 1).any()):
            joydf.append(df.loc[[i]])
        elif((df.loc[[i]]['EMOT'] == 2).any()):
            feardf.append(df.loc[[i]])
        elif((df.loc[[i]]['EMOT'] == 3).any()):
            angerdf.append(df.loc[[i]])
        elif((df.loc[[i]]['EMOT'] == 4).any()):
            saddf.append(df.loc[[i]])
        elif((df.loc[[i]]['EMOT'] == 5).any()):
            disgustdf.append(df.loc[[i]])
        elif((df.loc[[i]]['EMOT'] == 6).any()):
            shamedf.append(df.loc[[i]])
        else:
            guiltdf.append(df.loc[[i]])


trainJoy = joydf[0:int(round(len(joydf)*(2.0/3.0)))]
testJoy = joydf[int(round(len(joydf)*(2.0/3.0)))+1:]

trainFear = feardf[0:int(round(len(feardf)*(2.0/3.0)))]
testFear = feardf[int(round(len(feardf)*(2.0/3.0)))+1:]

trainAnger = angerdf[0:int(round(len(angerdf)*(2.0/3.0)))]
testAnger = angerdf[int(round(len(angerdf)*(2.0/3.0)))+1:]

trainSad = saddf[0:int(round(len(saddf)*(2.0/3.0)))]
testSad = saddf[int(round(len(saddf)*(2.0/3.0)))+1:]

trainDisgust = disgustdf[0:int(round(len(disgustdf)*(2.0/3.0)))]
testDisgust = disgustdf[int(round(len(disgustdf)*(2.0/3.0)))+1:]

trainShame = shamedf[0:int(round(len(shamedf)*(2.0/3.0)))]
testShame = shamedf[int(round(len(shamedf)*(2.0/3.0)))+1:]

trainGuilt = guiltdf[0:int(round(len(guiltdf)*(2.0/3.0)))]
testGuilt = guiltdf[int(round(len(guiltdf)*(2.0/3.0)))+1:]

testdf = testJoy + testFear + testAnger + testSad + testDisgust + testShame + testGuilt
labels = [1,2,3,4,5,6,7]
testLabels = np.repeat(labels,[len(testJoy),len(testFear),len(testAnger),len(testSad),len(testDisgust),len(testShame),len(testGuilt)], axis=0)

joyTrainCount = emotCount(trainJoy)
fearTrainCount = emotCount(trainFear)
angerTrainCount = emotCount(trainAnger)
sadTrainCount = emotCount(trainSad)
disgustTrainCount = emotCount(trainDisgust)
shameTrainCount = emotCount(trainShame)
guiltTrainCount = emotCount(trainGuilt)



pred = []
for i in range(0,len(testdf)):
    sentence = testdf[i]['SIT'].str.cat()
    sentence = re.sub(r"[^\w\d'\s]+",' ', sentence.lower()).split()
    sentence = [word for word in sentence if word not in stop]
    counts = [0,0,0,0,0,0,0]
    for j in range(0,len(sentence)):
        counts[0] += joyTrainCount[sentence[j]]
        counts[1] += fearTrainCount[sentence[j]]
        counts[2] += angerTrainCount[sentence[j]]
        counts[3] += sadTrainCount[sentence[j]]
        counts[4] += disgustTrainCount[sentence[j]]
        counts[5] += shameTrainCount[sentence[j]]
        counts[6] += guiltTrainCount[sentence[j]]
    pred.append(counts)

emotPred = []
correct = 0.0
for i in range(0,len(pred)):
    emotPred.append((pred[i].index(max(pred[i])))+1)
    if (emotPred[i] == testLabels[i]):
        correct += 1.0

correctPer = correct / len(testdf)
print('Percent Correctly Classified: ' + str(correctPer))





print('Finished')