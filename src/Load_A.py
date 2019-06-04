import numpy as np
import os
import matplotlib.pyplot as plt
from MyFunctions import *

#create variable to grab sample rate

'''Add user time selection functionality'''
def LoadRaw_1(fullPathName): #q1,samsung
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

def LoadRaw_2(fullPathName): #Data-008
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
def LoadRaw_3(fullPathName): #Top_right
    ''' gets rid of ; stop ... in csv file
    completed with a comment argument'''
    # unpack makes it column-major
    block =np.loadtxt( fullPathName,dtype=float, comments= ";", delimiter=',', usecols=(0,1,2,3), unpack=True)
    a = block[0:]
    return a

