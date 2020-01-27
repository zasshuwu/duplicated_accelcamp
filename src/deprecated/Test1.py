print ("hello")

import numpy as np
# unpack makes it column-major
block =np.loadtxt( "C:\svn\pythonDev1\PythonTestData1.csv", delimiter=',', usecols=(2,3,4,5), unpack=True, skiprows = 6  )

t= block[0]
a= block[1:]
ix=0
iy=1
iz=2

print (a[iz])


import matplotlib.pyplot as plt

plt.plot(t,a[iz])
plt.show()

a = np.array([4,5,6])
b = a
a = a+1

print(a[0],b[0], id(a), id(b))

a2 = np.array([4,5,6])
b2 = a2
a2[:] = a2+1

print(a2[0],b2[0], id(a2), id(b2), a2 is b2, 4 in a2, 5 in a2)

for n in a2:
    print(n)

np.savetxt('new.csv',block.transpose(),delimiter=',')

# vectorization tricks
# def oper( a ):
#     n = len(x)
#     x.append(0)
#     c = np.sin(x) + x*2+ y[n:]+3*x[1:]
#
#     for i = 1 range()

In [183]: arr = np.arange(10)

In [184]: np.save('some_array', arr)

If the file path does not already end in .npy, the extension will be appended. The array on disk can then be loaded using np.load:

In [185]: np.load('some_array.npy')
Out[185]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])