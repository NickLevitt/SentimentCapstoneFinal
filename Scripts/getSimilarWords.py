#http://www.nltk.org/howto/wordnet.html
#http://stackoverflow.com/questions/17864466/flatten-a-list-of-strings-and-lists-of-strings-and-lists-in-python
# Look in to ACL.org / ACM.org
from nltk.corpus import wordnet as wn

def flatten_to_strings(listOfLists):
    """Flatten a list of (lists of (lists of strings)) for any level
    of nesting"""
    result = []

    for i in listOfLists:
        # Only append if i is a basestring (superclass of string)
        if isinstance(i, basestring):
            result.append(i)
        # Otherwise call this function recursively
        else:
            result.extend(flatten_to_strings(i))
    return result


def getSimilar(wordlist):
    # Example wordlist: [u'happy',u'smile',u'joy', u'achievement',u'awesome',u'cheery',u'fun',u'funny',u'pleasant', u'paradise',u'tranquil']
    count = 0
    for i in range(0,2):
        for j in range(count,len(wordlist)):
            for ss in wn.synsets(wordlist[j]):
                temp = ss.lemma_names()
                count += 1
                for k in range(0,len(temp)):
                    wordlist.append(temp[k])


    return set(wordlist)