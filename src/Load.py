from LoadAccel import *
from LoadOmega import *
import numpy as np
import os
from MyFunctions import *
from tkinter import *

file_structure = "name.type.model.csv".split(".")
type_index = file_structure.index("type")
model_index = file_structure.index("model")

def LoadDataSet(dirpath=None):
    if(dirpath==None):
        root = Tk()
        root.withdraw()
        dirpath = filedialog.askdirectory(parent=root,initialdir="./",title='Please select a dataset')
    
    files = os.listdir(dirpath)
    print("-------Found "+str(len(files))+ " files-------")
    for i in files:
        print("Found: "+i)
    print("----------------------------")

    i = 1
    runs_files = []
    while(True):
        run = list(filter(lambda x: x == "run"+str(i), files))
        if(run != []):
            runs_files += run
        else:
            break
        i+=1
    print("Found "+str(len(runs_files))+" runs")
    runs_data = []
    for run in runs_files:
        print("-----------------"+run+"-----------------")
        runs_data.append(LoadRun(dirpath+"/"+run+"/"))
    return runs_data
        
def LoadRun(dirpath=None):
    if(dirpath==None):
        root = Tk()
        root.withdraw()
        dirpath = filedialog.askdirectory(parent=root,initialdir="./",title='Please select a run')

    files = os.listdir(dirpath)
    print("-------Found "+str(len(files))+ " files-------")
    for i in files:
        print("Found: "+i)
    print("----------------------------")
    accels_files = list(filter(lambda x: x.split(".")[type_index]=="accel", files))
    accels_data = []
    for file in accels_files:
        print("processing "+file+"...")
        accels_data.append(Load_Any(model=file.split(".")[model_index].capitalize(), filepath=dirpath+"/"+file))

    omega_files = list(filter(lambda x: x.split(".")[type_index]=="omega", files))
    omega_data = []
    for file in omega_files:
        print("processing "+file+"...")
        omega_data.append(Load_Omega(filepath=str(dirpath+"/"+file)))

    return { "accel": accels_data, "omega": omega_data }    
