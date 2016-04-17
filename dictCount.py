from collections import Counter
from nltk.corpus import stopwords

def dictCount(words):
    stop = set(stopwords.words('english'))
    stopwordsfree_words = [word for word in words if word not in stop]

    counts = Counter(stopwordsfree_words)

    return(counts)



#http://codereview.stackexchange.com/questions/90692/removing-all-stopwords-from-a-list-of-words