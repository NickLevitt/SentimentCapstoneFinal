import re
from dictCount import dictCount


def emotCount(df, emotNum):
    emotString = ''

    for i in range(0,len(df)):
        emotString = emotString + ' ' + str(df[i]['SIT'].str.cat())

    cleanEmot = re.sub(r"[^\w\d'\s]+",' ', emotString.lower())
    cleanEmot = cleanEmot.split()
    emotCount = dictCount(cleanEmot)


    return(emotCount)
