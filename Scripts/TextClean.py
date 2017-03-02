import os
import re
from nltk.corpus import stopwords

def textClean():
    storyList = []
    indxAdd1 = len("start of this project gutenberg ebook")
    stop = set(stopwords.words('english'))
    for data_file in os.listdir("./Stories/allStories"):
        if data_file[len(data_file)-3:] == 'txt':
            with open('./Stories/allStories/' + data_file, 'r') as file:
                text = file.read().lower()
                file.close()
                text = re.sub('[^a-z\ \']+', " ", text)
                #Remove Intro About Gutenberg
                try:
                    indx1 = text.index("start of this project gutenberg ebook")
                    indx2 = text.index("end of this project gutenberg ebook")
                except ValueError:
                    indx1 = text.index("start of the project gutenberg ebook")
                    indx2 = text.index("end of the project gutenberg ebook")

                text = text[indx1+indxAdd1:indx2]
                words = list(text.split())
                words = [word for word in words if word not in stop]
                storyList.append(words)

    return storyList





