
import numpy as np



def plottest():
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(0, 3 * np.pi, 500)
    y1 = np.sin(x)
    y2 = np.sin(3 * x)

    fig, ax = plt.subplots()
    ax.fill(x, y1, 'b', x, y2, 'r', alpha=0.3)
    plt.show()
    return

def LoadArray_GCDCBlue( fullPathName ):

    # unpack makes it column-major
    block =np.loadtxt( fullPathName, delimiter=',', usecols=(1,2,3,4), unpack=True, skiprows = 11  )

#    t= block[0]
#    ax= block[1]
#    ay= block[2]

    return block

def LoadArray( fullPathName ):

    # unpack makes it column-major
    block =np.loadtxt( fullPathName, delimiter=',', usecols=(2,3,4,5), unpack=True, skiprows = 6  )

    t= block[0]
    a= block[1:]
    ix=0
    iy=1
    iz=2
    return a

def runningAverage(a: object, window_len: object) -> object:

    w=np.ones(window_len,'d')

    y=np.convolve(w/w.sum(),a,mode='valid')
    #
   # y[:}=np.convolve(w/w.sum(),a,mode='valid')

    return y


from tkinter import filedialog
from tkinter import *
import os

dialogOpenDefaultOptions = {}
dialogOpenDefaultOptions['defaultextension'] = '.txt'
dialogOpenDefaultOptions['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
dialogOpenDefaultOptions['initialdir'] = os.getcwd()


dialogOpenDefaultOptions['title'] = 'This is a title'

def dialogOpenFilename( usrOptions = dialogOpenDefaultOptions ):

    if( usrOptions is not dialogOpenDefaultOptions):
        for k, v in dialogOpenDefaultOptions.items():
            if( k not in usrOptions):
                usrOptions[k]=v

    root = Tk()
    root.withdraw()
    usrOptions['parent'] = root

    return filedialog.askopenfilename(**usrOptions)

def min_lambda(key, array):
    return sorted(array, key=key)[0]
# if main()..
#plottest()