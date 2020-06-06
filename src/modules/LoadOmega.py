import numpy as np
from modules.Tools import dialogOpenFilename
from modules.DataStructures import RotaryData

def Load_Omega(filepath=None):
    if(filepath == None):
        filepath = dialogOpenFilename()
    block = np.loadtxt(filepath, dtype=float, delimiter=',', usecols=(0,1), unpack=True, skiprows=2)
    return RotaryData(block[0], block[1])
