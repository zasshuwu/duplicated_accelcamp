import tkinter as tk
from modules.Load import *
from modules.Tools import *
from modules.Plotter import *

defaultdir = "../../doc/Alphabet/data"
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(parent=root,initialdir=defaultdir,title='Please select a run')

run = LoadRun(file_path)
Plot(run["accel"])

'''fig = plt.figure()
#x, y, z = np.loadtxt(file_path, delimiter=',', unpack=True)
x,y=np.loadtxt(file_path, delimiter=',')
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()'''