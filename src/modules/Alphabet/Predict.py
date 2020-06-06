import tkinter as tk
from tkinter import filedialog
import csv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
import pickle
import cv2
import numpy


def Image(data):
    lastIndex = len(data.split('/')) - 1
    v0 = [0, 0, 0]
    x0 = [0, 0, 0]
    fToA = 1
    error = 0.28
    errorZ = 3
    t = []
    time = []
    m = [[] for i in range(3)]
    magnitude = [[] for i in range(3)]


    shift_x = 0
    shift_y = 0
    # For when the data starts at (2,1)
    if data.split('/')[lastIndex].split('.')[2] == "pocket":
        shift_x = 2
        shift_y = 1
        error = 0.3
        fToA = 1
    # For when the data starts at (0,0)
    elif data.split('/')[lastIndex].split('.')[2] == "pocket_mobile":
        shift_x = 0
        shift_y = 0
        error = 0.3
        fToA = 1
    # For when the data starts at (1,0)
    elif data.split('/')[lastIndex].split('.')[2] == "android":
        shift_x = 0
        shift_y = 1
        error = 0.02
        fToA = 9.81
        errorZ = 100

    shift = 0
    uselessboolean = True
    with open("input/" + data, 'r+') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if shift < shift_y:
                shift += 1
            else:
                t = row[shift_x]
                m[0] = row[1 + shift_x]
                m[1] = row[2 + shift_x]
                m[2] = row[3 + shift_x]
                time.append(float(t))
                for i in range(0, 3):
                    magnitude[i].append(float(m[i]) if abs(float(m[i])) > error else 0)


    acceleration = [[(j * fToA) for j in i] for i in magnitude]
    acceleration[2] = [i - 9.805 for i in acceleration[2]]

    # Translates Data into Position
    velocity = [[0 for i in time] for i in range(3)]
    position = [[0 for i in time] for i in range(3)]

    for j in range(3):
        velocity[j][0] = v0[j]
        for i in range(1, len(time)):
            velocity[j][i] = velocity[j][i - 1] + acceleration[j][i - 1] * (time[i] - time[i - 1])
    for j in range(3):
        position[j][0] = x0[j]
        for i in range(1, len(time)):
            position[j][i] = position[j][i - 1] + velocity[j][i - 1] * (time[i] - time[i - 1])
    for i in range(len(acceleration[2])):
        if abs(velocity[2][i]) > errorZ:
            position[0][i] = 0
            position[1][i] = 0
    plt.plot(position[0], position[1])
    plt.axis('off')
    plt.savefig("images/" + data + ".png")


root = tk.Tk()
root.withdraw()
dir_path = filedialog.askdirectory(title = "Select your Dataset")
info = os.listdir(dir_path)

for i in info:
    Image(i)

path, dirs, files = next(os.walk("./images"))
files.sort()

# Select a model
dir_path = filedialog.askopenfilename(title = "Choose your model") 

# Implement the model
pickle_in = open(dir_path, "rb")
mlp2 = pickle.load(pickle_in)

# Processes all the scanned images and adds them to the handwritten_story
handwritten_story = []
for i in range(len(files)):
    img = cv2.imread("./images/" + files[i], cv2.IMREAD_GRAYSCALE)
    handwritten_story.append(img)

print("Imported the scanned images.")

typed_story = ""
for letter in handwritten_story:
  letter = cv2.resize(letter, (28,28), interpolation = cv2.INTER_CUBIC)
    
  # Checks to see if the image is just a blank space by looking at the color of all the pixels summed
  total_pixel_value = 0
  for j in range(28):
    for k in range(28):
      total_pixel_value += letter[j,k]
  if total_pixel_value < 20:
    typed_story = typed_story + " "
  else:         
    single_item_array = (numpy.array(letter)).reshape(1, 784)
    prediction = mlp2.predict(single_item_array)
    typed_story = typed_story + str(chr(prediction[0] + 96))
    
print("Conversion to typed story complete.")
print(typed_story)
