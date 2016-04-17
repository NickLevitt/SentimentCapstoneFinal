import numpy as np
import re
import itertools
from collections import Counter


def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()


# def load_data_and_labels():
#     """
#     Loads MR polarity data from files, splits the data into words and generates labels.
#     Returns split sentences and labels.
#     """
#     # Load data from files
#     positive_examples = list(open("./data/rt-polaritydata/rt-polarity.pos", "r").readlines())
#     positive_examples = [s.strip() for s in positive_examples]
#     negative_examples = list(open("./data/rt-polaritydata/rt-polarity.neg", "r").readlines())
#     negative_examples = [s.strip() for s in negative_examples]
#     # Split by words
#     x_text = positive_examples + negative_examples
#     x_text = [clean_str(sent) for sent in x_text]
#     x_text = [s.split(" ") for s in x_text]
#     # Generate labels
#     positive_labels = [[0, 1] for _ in positive_examples]
#     negative_labels = [[1, 0] for _ in negative_examples]
#     y = np.concatenate([positive_labels, negative_labels], 0)
#     return [x_text, y]

def load_data_and_labels():
    """
    Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # JOY FEAR ANGER SADNESS DISGUST SHAME GUILT
    # Load data from files
    joy_examples = list(open("./data/emotdata/joy.txt", "r").readlines())
    joy_examples = [s.strip() for s in joy_examples]

    fear_examples = list(open("./data/emotdata/fear.txt", "r").readlines())
    fear_examples = [s.strip() for s in fear_examples]

    anger_examples = list(open("./data/emotdata/anger.txt", "r").readlines())
    anger_examples = [s.strip() for s in anger_examples]

    sad_examples = list(open("./data/emotdata/sad.txt", "r").readlines())
    sad_examples = [s.strip() for s in sad_examples]

    disgust_examples = list(open("./data/emotdata/disgust.txt", "r").readlines())
    disgust_examples = [s.strip() for s in disgust_examples]

    shame_examples = list(open("./data/emotdata/shame.txt", "r").readlines())
    shame_examples = [s.strip() for s in shame_examples]

    guilt_examples = list(open("./data/emotdata/guilt.txt", "r").readlines())
    guilt_examples = [s.strip() for s in guilt_examples]
    # Split by words
    x_text = joy_examples + fear_examples + anger_examples + sad_examples + disgust_examples + shame_examples + guilt_examples
    x_text = [clean_str(sent) for sent in x_text]
    x_text = [s.split(" ") for s in x_text]
    # Generate labels
    joy_labels = [[1, 0, 0, 0, 0, 0, 0] for _ in joy_examples]
    fear_labels = [[0, 1, 0, 0, 0, 0, 0] for _ in fear_examples]
    anger_labels = [[0, 0, 1, 0, 0, 0, 0] for _ in anger_examples]
    sad_labels = [[0, 0, 0, 1, 0, 0, 0] for _ in sad_examples]
    disgust_labels = [[0, 0, 0, 0, 1, 0, 0] for _ in disgust_examples]
    shame_labels = [[0, 0, 0, 0, 0, 1, 0] for _ in shame_examples]
    guilt_labels = [[0, 0, 0, 0, 0, 0, 1] for _ in guilt_examples]

    y = np.concatenate([joy_labels, fear_labels, anger_labels, sad_labels, disgust_labels, shame_labels, guilt_labels], 0)
    return [x_text, y]

def load_story_data_and_labels():
    """
    Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # JOY FEAR ANGER SADNESS DISGUST SHAME GUILT
    # Load data from files
    joy_examples = list(open("./data/emotdata/joy.txt", "r").readlines())
    joy_examples = [s.strip() for s in joy_examples]
    # Split by words
    x_text = joy_examples
    x_text = [clean_str(sent) for sent in x_text]
    x_text = [s.split(" ") for s in x_text]
    # Generate labels
    joy_labels = [[1, 0, 0, 0, 0, 0, 0] for _ in joy_examples]
    y = np.concatenate([joy_labels], 0)
    return [x_text, y]

def pad_sentences(sentences, padding_word="<PAD/>"):
    """
    Pads all sentences to the same length. The length is defined by the longest sentence.
    Returns padded sentences.
    """
    sequence_length = max(len(x) for x in sentences)
    padded_sentences = []
    for i in range(len(sentences)):
        sentence = sentences[i]
        num_padding = sequence_length - len(sentence)
        new_sentence = sentence + [padding_word] * num_padding
        padded_sentences.append(new_sentence)
    return padded_sentences


def build_vocab(sentences):
    """
    Builds a vocabulary mapping from word to index based on the sentences.
    Returns vocabulary mapping and inverse vocabulary mapping.
    """
    # Build vocabulary
    word_counts = Counter(itertools.chain(*sentences))
    # Mapping from index to word
    vocabulary_inv = [x[0] for x in word_counts.most_common()]
    # Mapping from word to index
    vocabulary = {x: i for i, x in enumerate(vocabulary_inv)}
    return [vocabulary, vocabulary_inv]

def pad_story(sentences, max_len, padding_word="<PAD/>"):
    """
    Pads all sentences to the same length. The length is defined by the longest sentence.
    Returns padded sentences.
    """
    sequence_length = max_len
    padded_sentences = []
    for i in range(len(sentences)):
        sentence = sentences[i]
        num_padding = sequence_length - len(sentence)
        new_sentence = sentence + [padding_word] * num_padding
        padded_sentences.append(new_sentence)
    return padded_sentences

def load_story(vocabulary, vocabulary_inv):
    story = list(open("/Users/nicklevitt/Desktop/SentimentCap/Stories/allStories/AliceInWonderland.txt", "r").readlines())
    story = [s.strip() for s in story]
    story = [clean_str(sent) for sent in story]
    story = [s.split(" ") for s in story]
    # TODO UPDATE SO ONLY PAD TO LENGTH OF MAX ISEAR SENTENCE, AS OF NOW I HAVE ADDED THE STORY DATA TO THE VOCABULARY
    story_pad = pad_story(story, 179)
    x = np.array([[vocabulary[word] for word in sentence] for sentence in story_pad])
    return x

def build_input_data(sentences, labels, vocabulary):
    """
    Maps sentencs and labels to vectors based on a vocabulary.
    """
    x = np.array([[vocabulary[word] for word in sentence] for sentence in sentences])
    y = np.array(labels)
    return [x, y]

def load_story_data():
    # Load and preprocess data
    story = list(open("/Users/nicklevitt/Desktop/SentimentCap/Stories/allStories/AliceInWonderland.txt", "r").readlines())
    story = [s.strip() for s in story]
    story = [clean_str(sent) for sent in story]
    story = [s.split(" ") for s in story]
    # TODO UPDATE SO ONLY PAD TO LENGTH OF MAX ISEAR SENTENCE, AS OF NOW I HAVE ADDED THE STORY DATA TO THE VOCABULARY
    story_pad = pad_story(story, 179)
    sentences, labels = load_data_and_labels()
    sentences_padded = pad_sentences(sentences)
#    vocabulary, vocabulary_inv = build_vocab(sentences_padded)
    final_sent = sentences_padded + story_pad
    vocabulary, vocabulary_inv = build_vocab(final_sent)
    x, y = build_input_data(sentences_padded, labels, vocabulary)
    return [x, y, vocabulary, vocabulary_inv]


def load_data():
    """
    Loads and preprocessed data for the MR dataset.
    Returns input vectors, labels, vocabulary, and inverse vocabulary.
    """
    # Load and preprocess data
    sentences, labels = load_data_and_labels()
    # TODO UPDATE SO ONLY PAD TO LENGTH OF MAX ISEAR SENTENCE, AS OF NOW I HAVE ADDED THE STORY DATA TO THE VOCABULARY
    sentences_padded = pad_sentences(sentences)
#    vocabulary, vocabulary_inv = build_vocab(sentences_padded)
    vocabulary, vocabulary_inv = test_vocab(sentences_padded)
    x, y = build_input_data(sentences_padded, labels, vocabulary)
    return [x, y, vocabulary, vocabulary_inv]


def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int(len(data)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]
