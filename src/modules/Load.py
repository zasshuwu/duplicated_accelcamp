from modules.LoadAccel import *
from modules.LoadOmega import *
import os
from tkinter import *



defaultdir = "../data"



def LoadDataSet(dirpath=None):
    if(dirpath==None):
        root = Tk()
        root.withdraw()
        dirpath = filedialog.askdirectory(parent=root,initialdir=defaultdir,title='Please select a dataset')
    
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


# load a single AccelData object and RotaryData object
# simpler front-end for LoadRun()
def LoadSingleRun( dirpath=None):
    run = LoadRun(dirpath)
    return { "accel": run["accel"][0], "omega": run["omega"][0]}

# deprecated:
def LoadRun(dirpath=None):
    return LoadMultiRun(dirpath)

# Load multiple runs as a list of AccelData objects and list of RotaryData objects
def LoadMultiRun(dirpath=None):
    if(dirpath==None):
        root = Tk()
        root.withdraw()
        dirpath = filedialog.askdirectory(parent=root,initialdir=defaultdir,title='Please select a run')

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
        data = LoadAccelFile(dirpath+"/"+file)
        if(data != "Model is not currently supported"):
            accels_data.append(data)
        else:
            print("Failed to Load: "+file+" (Model not supported)")

    omega_files = list(filter(lambda x: x.split(".")[type_index]=="omega", files))
    omega_data = []
    for file in omega_files:
        print("processing "+file+"...")
        omega_data.append(Load_Omega(filepath=str(dirpath+"/"+file)))

    if accels_data == [] and omega_data == []:
        raise FileNotFoundError('No files were found.')

    return {"accel": accels_data, "omega": omega_data}
