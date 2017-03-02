import os
import re
from nltk.corpus import stopwords

def cleanLunch():
    storyList = []
    indxAdd1 = len("start of this project gutenberg ebook")
    stop = set(stopwords.words('english'))
    for data_file in os.listdir("./Stories/lunchStories"):
        if data_file[len(data_file)-3:] == 'txt':
            with open('./Stories/lunchStories/' + data_file, 'r') as file:
                text = file.read().lower()
                file.close()
                text = re.sub('[^a-z\ \']+', " ", text)
                #Remove Intro About Gutenberg
                words = list(text.split())
                words = [word for word in words if word not in stop]
                storyList.append(words)

    return storyList





