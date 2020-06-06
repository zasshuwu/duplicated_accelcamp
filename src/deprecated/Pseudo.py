import matplotlib.pyplot as plt
from modules.Tools import *

#create variable to grab sample rate

'''Add user time selection functionality'''
def LoadRaw_1( fullPathName):
    # unpack makes it column-major
    block =np.loadtxt( fullPathName,dtype=float, comments= ";", delimiter=',', usecols=(0,1,2,3), unpack=True,
                       skiprows=1)
    #current file is q1
    #skipping 10 rows is device specific
    a= block[0:] #a[0] is time
    ix=0
    iy=1
    iz=2
    return a

def LoadRaw_2( fullPathName):
    ''' gets rid of ; stop ... in csv file
    completed with a comment argument'''
    # unpack makes it column-major
    block =np.loadtxt( fullPathName,dtype=float, comments= ";", delimiter=',', usecols=(0,1,2,3), unpack=True,
                       skiprows=10)
    #current file is TopRight_Feb18
    #skipping 10 rows is device specific
    a= block[0:] #a[0] is time
    ix=0
    iy=1
    iz=2
    return a
def LoadRaw_3( fullPathName):
    ''' gets rid of ; stop ... in csv file
    completed with a comment argument'''
    # unpack makes it column-major
    block =np.loadtxt( fullPathName,dtype=float, comments= ";", delimiter=',', usecols=(0,1,2,3), unpack=True,
                       skiprows=9)
    #current file is TopRight_Feb18
    #skipping 10 rows is device specific
    a= block[0:] #a[0] is time
    ix=0
    iy=1
    iz=2
    return a
'''
try:
    for i in :
        if i == "Time":
            LoadRaw_1
'''

'''after this the script should run perfectly, the LoadRaw function is the determining factor'''

# -- open file --
myOpts = {}
myOpts['initialfile'] = 'TopRight_Feb18.csv'
'''Test file was TopRight_Feb18.csv'''
fullPathName = dialogOpenFilename(myOpts)
# for dev. purposes, skip dialog and use in-code filename
#fName = "PythonTestData1.csv"
#fullPathName = os.getcwd + "\\" + fName

# b = LoadArray_GCEDCDblue(filename)
#   t= block[0]
# #    ax= block[1]
# #    ay= block[2]
a = LoadRaw_3(fullPathName)
times = a[0]

print(a)

'''Asks for outer radius'''
try:
    Rdx = input("What was the Rdx in mm?")
    Rdy = input("What was the Rdy in mm?")
    Rdx_int = int(Rdx)
    Rdy_int = int(Rdy)
    print("Rdx is %s \nRdy is %s" %(Rdx, Rdy))
except ValueError:
    print("A number was not entered")
    Rdx = input("What was the Rdx?")
    Rdy = input("What was the Rdy?")



'''Graphing ax vs t and ay vs t'''
time = a[0]
ax = a[1]
ay = a[2]
'''display graphs before user times'''
avg_ax = np.average(ax)
avg_ay = np.average(ay)
print("The average acceleration in x is %s\nThe average acceleration in y is %s" %(avg_ax,avg_ay))
#plt.title('raw data: close window to show RMS analysis')
plt.subplot(2,1,1)
plt.plot(time,ax, label="Accel in x")
plt.minorticks_on()
plt.grid(b=True, which='both', color='0.65',linestyle='-')
plt.xlabel("Time")
plt.ylabel("Acceleration in x-direction")
ax_mean = [np.mean(ax)]*len(time)
ax_mean_line = plt.plot(time,ax_mean, label='Mean', linestyle='--')
plt.legend(['Acceleration in x', 'Average in x'])

plt.subplot(2,1,2)
plt.subplots_adjust(hspace=0.3)
plt.plot(time,ay, label='Accel in y')
plt.minorticks_on()
plt.grid(b=True, which='both', color='0.65',linestyle='-')
plt.xlabel("Time")
plt.ylabel("Acceleration in y-direction")
ay_mean = [np.mean(ay)]*len(time)
ay_mean_line = plt.plot(time,ay_mean, label='Mean', linestyle='--')
plt.legend(['Acceleration in y', 'Average in y'])
plt.ioff()
plt.show()
print("time")
try:
    Start = input("Starting time")
    End = input("End time")
    Start_int = int(Start)
    End_int = int(End)
    print("Start is %s seconds\nEnd is %s seconds" %(Start, End))
except ValueError:
    print("A time was not entered")
    Start = input("Starting time")
    End = input("End time")

'''user selected time'''
n=0
avg_x = 0
avg_x_2 = 0
for i in range(len(time)):
 if( time[i]>Start_int and time[i]<End_int):
    avg_x += ax[i]
    n+=1
avg_x/=n
print("avg and n ", avg_x, n)


avg_x_2 = ax[(time>Start_int) & (time<End_int)].mean()
print("method 1: " + str(avg_x))
print("method 2: " + str(avg_x_2))

