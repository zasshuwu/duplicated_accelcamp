import os
import numpy
import tkinter as tk
from tkinter import filedialog
from emnist import extract_training_samples
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
import cv2
import pickle

X, y = extract_training_samples('letters')
name = input("Name your model")

# Make sure that every pixel in all of the images is a value between 0 and 1
X = X / 255.

# Use the first 60000 instances as training and the next 10000 as testing
X_train, X_test = X[:60000], X[60000:70000]
y_train, y_test = y[:60000], y[60000:70000]

# Record the number of samples in each dataset and the number of pixels in each image
X_train = X_train.reshape(60000,784)
X_test = X_test.reshape(10000,784)

print("Extracted our samples and divided our training and testing data sets")

mlp2 = MLPClassifier(hidden_layer_sizes=(100,100,100,), max_iter=50, alpha=1e-1,
                    solver='sgd', verbose=10, tol=1e-4, random_state=1,
                    learning_rate_init=0.8)

mlp2.fit(X_train, y_train)
print("Training set score: %f" % mlp2.score(X_train, y_train))
print("Test set score: %f" % mlp2.score(X_test, y_test))

# Save the model
with open( "models/" + name + ".pickle", "wb") as f:
    pickle.dump(mlp2, f)