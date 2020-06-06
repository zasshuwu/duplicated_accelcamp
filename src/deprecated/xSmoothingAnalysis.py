import matplotlib.pyplot as plt
from modules.Tools import *

# -- open file --
myOpts = {}
myOpts['initialfile'] = 'PythonTestData1.csv'
fullPathName = dialogOpenFilename(myOpts)
# for dev. purposes, skip dialog and use in-code filename
#fName = "PythonTestData1.csv"
#fullPathName = os.getcwd + "\\" + fName

# b = LoadArray_GCEDCDblue(filename)
#   t= block[0]
# #    ax= block[1]
# #    ay= block[2]

a = LoadArray(fullPathName)
az = a[2]

plt.title('raw acceleration vs. time data: close window to show RMS analysis')
plt.plot(az)
plt.minorticks_on()
plt.grid(b=True, which='both', color='0.65',linestyle='-')
plt.show()

# compute RMS for each window_len value, plot

window_lengths = np.arange(1,300,1)
# circular list


#cwdx = "C:\\svn\\pythonDev1\\"
#np.save(cwd+"data1",az )

#aznew = np.load(cwd+"data1.npy")

RMS=np.empty( window_lengths.size)
#y = np.empty_like(window_lengths) # not necessary, new array created each time anyway..

for i, length in enumerate(window_lengths):
    y = runningAverage(az, length)
    RMS[i] = np.std(y)

deriv_shorterByTwo = np.diff(RMS,n=2)
pad = np.full(2,deriv_shorterByTwo[-1])
deriv = np.append(deriv_shorterByTwo,pad)

plt.clf()

d = dict(markersize=.7, label="RMS")
plt.xlabel('window length in #samples')
plt.ylabel('RMS/std value')
plt.title('RMS vs. running-average length')
plt.plot(window_lengths,RMS,'ro', **d)


scaleFactor = 20
plt.plot(window_lengths,scaleFactor*deriv, label= "RMS derivative")
plt.minorticks_on()
plt.grid(b=True, which='major', color='b', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')
plt.legend() # this call relies on kw "label" of function plot() # in order to have a visible effect
plt.show()


