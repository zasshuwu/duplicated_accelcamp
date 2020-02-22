import numpy as np
from modules.Tools import dialogOpenFilename
from modules.DataStructures import AccelData

# structure we impose on data filenames
file_structure = "name.type.model.csv".split(".")
type_index = file_structure.index("type")
model_index = file_structure.index("model")


def LoadAccelFile(filename):
    modelType = filename.split("/")[-1].split(".")[model_index].capitalize()
    try:
        accelData = eval(Model_Dict[modelType] + "'" + filename + "')")
    except KeyError:
        return "Model is not currently supported"
    return accelData


# def Load_Any(model,filepath=""):
#     try:
#         return eval(Model_Dict[model]+"'"+filepath+"')")
#     except KeyError:
#         return "Model is not currently supported"


########### individual load functions for each sensor type #########################

def Load_X(filepath=None):
    if filepath is None:
        filepath = dialogOpenFilename()

    block = np.loadtxt(filepath, dtype=float, comments=";", delimiter=',', usecols=(0, 1, 2, 3), unpack=True)
    # a = [ax, ay, az] | t = [t]
    a = block[1:]
    t = block[0]
    t0 = t[0]
    for y in range(len(t)):
        t[y] -= t0

    return AccelData(t, a.transpose(), "X")


def Load_Samsung(filepath=None):
    if filepath is None:
        filepath = dialogOpenFilename()

    block = np.loadtxt(filepath, dtype=float, delimiter=',', usecols=(0, 1, 2, 3), unpack=True, skiprows=1)
    # a = [ax, ay, az] | t = [t]
    a = block[1:]
    t = block[0]
    t0 = t[0]
    for y in range(len(t)):
        t[y] -= t0

    a *= 9.807
    return AccelData(t, a.transpose(), "Samsung")


def Load_X16(filepath=None):
    # Since Load_X works with X16s, it just returns Load_X()
    data = Load_X(filepath)
    data.model = "X16"
    return data


def Load_X2(filepath=None):
    # Since Load_X works with X2s, it just returns Load_X()
    # Assuming X2 has High Gain (counts/13108)
    data = Load_X(filepath)

    data.a /= 13108
    data.a *= 9.807
    data.model = "X2"

    return data


def Load_Pocket(filepath=None):
    if (filepath == None):
        filepath = dialogOpenFilename()

    block = np.loadtxt(filepath, dtype=float, delimiter=',', usecols=(2, 3, 4, 5), unpack=True, skiprows=1)
    # a = [ax, ay, az] | t = [t]
    a = block[1:]
    t = block[0]
    t0 = t[0]
    for y in range(len(t)):
        t[y] -= t0
    return AccelData(t, a.transpose(), "Pocket Lab")

def Load_PocketMobile(filepath=None):
    if (filepath == None):
        filepath = dialogOpenFilename()

    block = np.loadtxt(filepath, dtype=float, delimiter=',', usecols=(0, 1, 2, 3), unpack=True, skiprows=1)
    # a = [ax, ay, az] | t = [t]
    a = block[1:]
    t = block[0]
    t0 = t[0]
    for y in range(len(t)):
        t[y] -= t0
    return AccelData(t, a.transpose(), "Pocket Lab")

# mapping of accelerometer sensor types to the names of the functions that load them
Model_Dict = {
    "X2":Load_X2,
    "X16":Load_X16,
    "Samsung":Load_Samsung,
    "Pocket":Load_Pocket,
    "Pocket_mobile":Load_PocketMobile
}