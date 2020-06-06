import matplotlib.pyplot as plt
from modules.Tools import *

def zkXLabelTime(plt):
    plt.xlabel(r'$time \ t \ \left(s\right)$')

def f(plt, string):
    plt.ylabel(r'$A_'+'z \   \left(m/s^2\right)$', fontweight='bold')

x2 = r'$A_' + v + r'\    \left(m/s^2\right)$'
#plt.ylabel(r'$A_x \   \left(m/s^2\right)$')
plt.ylabel(x2)

# -- open file --
myOpts = {}
myOpts['title'] = 'Select CVS source file'
myOpts['initialfile'] = 'PythonTestData1.csv'

fullPathName = dialogOpenFilename(myOpts)
a = LoadArray(fullPathName)
az = a[2]

# figsize is absolute size of individual plot figures
#fig, ax = plt.subplots(num=None, figsize=(9, 4), dpi=80, facecolor='w', edgecolor='k')
fig, ax = plt.subplots(num=None, dpi=80, facecolor='w', edgecolor='k')
fig.canvas.set_window_title('3-axis raw accelerometer data')
fig.suptitle('3-axis raw accelerometer data', fontsize=20)
fig.set_size_inches(10,10) # absolute size of the frame

# #ff5500ff

plt.rc("font", size=16)
#plt.rc("fontweight",'bold')
plt.subplots_adjust(top = .85, bottom = .1 , hspace = .71) # top

plt.subplot(3,1,1)
zkXLabelTime(plt)
zkYLabelAcceleration(plt,'x')
#plt.xlabel(r'$time \ t \ \left(s\right)$')
#f(plt,'d')
s1 = "r'$A_"
s2="x \   \left(m/s^2\right)$',fontweight='bold'"
s3=s1+s2

x = r'$A_    \left(m/s^2\right)$'
v='x'
x2 = r'$A_' + v + r'\    \left(m/s^2\right)$'
#plt.ylabel(r'$A_x \   \left(m/s^2\right)$')
plt.ylabel(x2)
plt.plot(a[0])

plt.subplot(3,1,2)
zkXLabelTime(plt)
plt.ylabel(r'$A_y \   \left(m/s^2\right)$',fontweight='bold')
plt.plot(a[1])

plt.subplot(3,1,3)
zkXLabelTime(plt)
plt.plot(a[2])
plt.ylabel(r'$A_z \   \left(m/s^2\right)$',fontweight='bold')
plt.show()

c= diff(a)
c=ediff