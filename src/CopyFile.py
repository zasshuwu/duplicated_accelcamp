import sys
import os
import shutil

# print os.dir

fileIn = sys.argv[1]
fileOut = fileIn + "aaa"

shutil.copy(fileIn, fileOut)
