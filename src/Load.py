from LoadAccel import *
from LoadOmega import *
import numpy as np
import os
from MyFunctions import *
from tkinter import *

file_structure = "name.type.model.csv".split(".")
type_index = file_structure.index("type")
model_index = file_structure.index("model")

def Load(dirpath=None):
    if(dirpath==None):
        root = Tk()
        root.withdraw()
        dirpath = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a dataset')

    files = os.listdir(dirpath)
    print("-------Found "+str(len(files))+ " files-------")
    for i in files:
        print("Found: "+i)
    print("----------------------------")

    i = 1
    runs_files = []
    while(True):
        run = list(filter(lambda x: "run"+str(i) in x, files))
        if(run != []):
            runs_files.append(run)
        else:
            break
        i+=1
    print("Found "+str(len(runs_files))+" runs")
    runs_data = []
    for run in runs_files:
        runs_data += LoadRun(dirpath+run+"/")
    return crun
        
def LoadRun(dirpath=None):
    if(dirpath==None):
        root = Tk()
        root.withdraw()
        dirpath = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a dataset')

    files = os.listdir(dirpath)
    print("-------Found "+str(len(files))+ " files-------")
    for i in files:
        print("Found: "+i)
    print("----------------------------")
    accels_files = list(filter(lambda x: x.slip(".")[type_index]=="accel", run))
    accels_data = []
    for file in accels_files:
        print("processing "+file+"...")
        accels_data += Load_Any(model=file.split(".")[model_index].capitalize(), filepath=dirpath+"/"+file)

    omega_files = list(filter(lambda x: x.slip(".")[type_index]=="omega", run))
    omega_data = []
    for file in accels_files:
        print("processing "+file+"...")
        omega_data += Load_Omega(filepath=dirpath+"/"+file)

    return { "accel": accels_data, "omega": omega_data }    
