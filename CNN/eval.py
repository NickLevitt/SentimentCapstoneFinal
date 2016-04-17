#! /usr/bin/env python

import tensorflow as tf
import numpy as np
import os
import time
import datetime
import data_helpers

from text_cnn import TextCNN

# Parameters
# ==================================================

# Eval Parameters
tf.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
tf.flags.DEFINE_string("checkpoint_dir", "/Users/nicklevitt/Desktop/SentimentCap/CNN/runs/1460654314/checkpoints", "Checkpoint directory from training run")

# Misc Parameters
tf.flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
tf.flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")


FLAGS = tf.flags.FLAGS
FLAGS._parse_flags()
print("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
    print("{}={}".format(attr.upper(), value))
print("")

# this should WORK TO LOAD THE HELD-OUT (1/3) DATA FROM ISEAR TO CHECK ACCURACY. HOPE IT WORKS LOLOLOLOL
x, y, vocabulary, vocabulary_inv = data_helpers.load_story_data()
# Randomly shuffle data
np.random.seed(10)
shuffle_indices = np.random.permutation(np.arange(len(y)))
x_shuffled = x[shuffle_indices]
y_shuffled = y[shuffle_indices]
testindx = int(round(float(len(x_shuffled)) * (.3333)))
x_test = x_shuffled[-testindx:]
y_test = y_shuffled[-testindx:]

# Load data. Load your own data here THIS IS FOR LOADING THE STORY DATA TO TEST
# print("Loading data...")
# x_test, y_test, vocabulary, vocabulary_inv = data_helpers.load_story_data()
# # TODO STORY X-TEST HERE
# x_test = data_helpers.load_story(vocabulary, vocabulary_inv)

y_test = np.argmax(y_test, axis=1)
print("Vocabulary size: {:d}".format(len(vocabulary)))
print("Test set size {:d}".format(len(y_test)))

print("\nEvaluating...\n")

# Evaluation
# ==================================================
checkpoint_file = tf.train.latest_checkpoint(FLAGS.checkpoint_dir)
graph = tf.Graph()
with graph.as_default():
    session_conf = tf.ConfigProto(
      allow_soft_placement=FLAGS.allow_soft_placement,
      log_device_placement=FLAGS.log_device_placement)
    sess = tf.Session(config=session_conf)
    with sess.as_default():
        # Load the saved meta graph and restore variables
        # saver = tf.train.import_meta_graph("{}.meta".format(checkpoint_file))
        # TODO NEED TO UPDATE THIS
        saver = tf.train.import_meta_graph("/Users/nicklevitt/Desktop/SentimentCap/CNN/runs/1460654314/checkpoints/model-12600.meta")
        saver.restore(sess, checkpoint_file)

        # Get the placeholders from the graph by name
        input_x = graph.get_operation_by_name("input_x").outputs[0]
        # input_y = graph.get_operation_by_name("input_y").outputs[0]
        dropout_keep_prob = graph.get_operation_by_name("dropout_keep_prob").outputs[0]

        # Tensors we want to evaluate
        predictions = graph.get_operation_by_name("output/predictions").outputs[0]

        # Generate batches for one epoch
        batches = data_helpers.batch_iter(x_test, FLAGS.batch_size, 1, shuffle=False)

        # Collect the predictions here
        all_predictions = []

        for x_test_batch in batches:
            batch_predictions = sess.run(predictions, {input_x: x_test_batch, dropout_keep_prob: 1.0})
            all_predictions = np.concatenate([all_predictions, batch_predictions])

# Print accuracy
correct_predictions = sum(all_predictions == y_test)
print("Total number of test examples: {}".format(len(y_test)))
print("Accuracy: {:g}".format(float(correct_predictions)/float(len(y_test))))
