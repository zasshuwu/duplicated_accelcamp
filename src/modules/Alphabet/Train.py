import os
import numpy
import tkinter as tk
from tkinter import filedialog
from emnist import extract_training_samples
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
import cv2
import pickle

path, dirs, files = next(os.walk("./letters_mod"))
files.sort()
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

mlp2 = MLPClassifier(hidden_layer_sizes=(150,150,150,150,150,), max_iter=50, alpha=1e-4,
                    solver='sgd', verbose=10, tol=1e-4, random_state=1,
                    learning_rate_init=0.1)

mlp2.fit(X_train, y_train)
print("Training set score: %f" % mlp2.score(X_train, y_train))
print("Test set score: %f" % mlp2.score(X_test, y_test))

# Processes all the scanned images and adds them to the handwritten_story
handwritten_story = []
for i in range(len(files)):
    img = cv2.imread("./letters_mod/" + files[i], cv2.IMREAD_GRAYSCALE)
    handwritten_story.append(img)

# Save the model
with open( "models/" + name + ".pickle", "wb") as f:
    pickle.dump(mlp2, f)