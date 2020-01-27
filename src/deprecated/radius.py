import matplotlib.pyplot as plt
from Simulate import *
from Curvature import *
import numpy as np
from tkinter import filedialog



a = convertOmegaAccel(simConstAlpha(
                int(input("Number of iterations: ")),
                np.float32(input("Delta t: ")),
                np.float32(input("alpha: ")),
                np.float32(input("omega at t=0: "))
            ), np.float32(input("Radius: ")))

adot = np.square(GenADot(a))
yx2 = Genyx2(a)

r_val = 4*adot/yx2
print(len(r_val)-len(a.a[0]))
path = filedialog.asksaveasfilename(initialdir = "../")
np.savetxt(path+".csv", np.array([r_val,a.a[0][:-1],a.a[1][:-1]]), delimiter=",",fmt="%.18f")


plt.plot(a.t[:-2],r_val)

plt.xlabel("Time (s)")
plt.ylabel("Radius (m))", fontsize=8)
plt.xlim(0,np.max(a.t))
#plt.show(block=False)
plt.show()


