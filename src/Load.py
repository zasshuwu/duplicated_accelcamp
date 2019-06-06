from LoadAccel import *
from LoadOmega import *
import numpy as np
import os
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
        print("\n\n-----------------"+run+"-----------------")
        runs_data.append(LoadRun(dirpath+"/"+run+"/"))
    return runs_data
        
def LoadRun(dirpath=None):
    if(dirpath==None):
        root = Tk()
        root.withdraw()
        dirpath = filedialog.askdirectory(parent=root,initialdir="./",title='Please select a run')

    found_files = os.listdir(dirpath)
    print("-------Found "+str(len(found_files))+ " files-------")
    for i in found_files:
        print("Found: "+i)
    print("The Following Files Will be Ignored:")
    not_file = list(filter(lambda x: ((x.split(".")[type_index]!="accel" and
                                      x.split(".")[type_index]!="omega") or
                                      x.split(".")[-1].lower()!="csv" or
                                      len(x.split(".")) != 4
                                      ),
                           found_files))
    for i in not_file:
        print("- "+i+("(Wrong File Structure)" if len(i.split(".")) != 4
                      else "(Wrong File Format)" if i.split(".")[-1].lower()!="csv"
                      else "(Unsupported Type)" if i.split(".")[type_index]!="accel" and i.split(".")[type_index]!="omega"
                      else ""
                        ))
    if(not_file == []):
        print("--None--")

    print("----------------------------")
    files = list(filter(lambda x: not_file.count(x) == 0,
                           found_files))
    accels_files = list(filter(lambda x: x.split(".")[type_index]=="accel", files))
    accels_data = []
    for file in accels_files:
        print("processing "+file+"...")
        data = Load_Any(model=file.split(".")[model_index].capitalize(), filepath=dirpath+"/"+file)
        if(data != "Model is not currently supported"):
            accels_data.append(data)
        else:
            print("Failed to Load: "+file+" (Model not supported)")

    omega_files = list(filter(lambda x: x.split(".")[type_index]=="omega", files))
    omega_data = []
    for file in omega_files:
        print("processing "+file+"...")
        omega_data.append(Load_Omega(filepath=str(dirpath+"/"+file)))

    return { "accel": accels_data, "omega": omega_data }    
