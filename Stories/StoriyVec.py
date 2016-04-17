import gensim
import os
import numpy as np
import nltk
from gensim.models.word2vec import Word2Vec
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

class MySentences(object):
     def __init__(self, dirname):
         self.dirname = dirname

     def __iter__(self):
         for fname in os.listdir(self.dirname):
             for line in open(os.path.join(self.dirname, fname)):
                 yield line.split()

sentences = MySentences('/Users/nicklevitt/Desktop/School/Senior/Spring/Capstone/Stories/allStoriesx') # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences)

start = time.time() # Start time

word_vectors = model.syn0
num_clusters = 2 #Set to number of emotions being clustered
kmeans_clustering = KMeans( n_clusters = num_clusters )
idx = kmeans_clustering.fit_predict( word_vectors )




# with open('happy.txt', 'r') as infile:
#     good_words = infile.read().splitlines()
#
# with open('negative.txt', 'r') as infile:
#     bad_words = infile.readlines()
#
# def getWordVecs(words):
#     vecs = []
#     for word in words:
#         word = word.replace('\n', '')
#         try:
#             vecs.append(model[word].reshape((1,len(vecs))))
#         except KeyError:
#             continue
#     vecs = np.concatenate(vecs)
#     return np.array(vecs, dtype='float') #TSNE expects float type values
#
# good_vecs = getWordVecs(good_words)
# bad_vecs = getWordVecs(bad_words)

# file_content = open("/Users/nicklevitt/Desktop/School/Senior/Spring/Capstone/Stories/allStories/AliceInWonderland.txt").read()
# tokens = nltk.word_tokenize(file_content)
# tagged = nltk.pos_tag(tokens)
# model = gensim.models.Word2Vec(tokens, size=200, min_count=1)
# model.most_similar(positive=['woman', 'king'], negative=['man'])


# documents = ["Human machine interface for lab abc computer applications",
#               "A survey of user opinion of computer system response time",
#               "The EPS user interface management system",
#               "System and human system engineering testing of EPS",
#               "Relation of user perceived response time to error measurement",
#               "The generation of random binary unordered trees",
#               "The intersection graph of paths in trees",
#               "Graph minors IV Widths of trees and well quasi ordering",
#               "Graph minors A survey"]
#
# file_content = open("/Users/nicklevitt/Desktop/School/Senior/Spring/Capstone/Stories/allStories/AliceInWonderland.txt").read()
#
#
# stoplist = set('for a of the and to in'.split())
# texts = [[word for word in document.lower().split() if word not in stoplist]
#           for document in file_content]
# from collections import defaultdict
# frequency = defaultdict(int)
# for text in texts:
#     for token in text:
#         frequency[token] += 1
#
# texts = [[token for token in text if frequency[token] > 1]
#          for text in texts]
#
# from pprint import pprint   # pretty-printer
# pprint(texts)
