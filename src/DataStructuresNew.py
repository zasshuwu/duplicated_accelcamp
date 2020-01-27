import numpy as np

# this file to replace the current "DataStructures.py"

############# tools to catch type erros in ndarray structures #########

# type "vec3" is restrictively defined to be an ndarray of 3 doubles
def isVec3( a : np.ndarray ) -> bool:
    if not isinstance(a,np.ndarray) : return False
    if len(np.shape(a)) != 1: return False
    if np.shape(a)[0] != 3: return False
    if a.dtype != np.double(999): return False
    return True

def isArrayOfVec3( a : np.ndarray ) -> bool:
    if not isinstance(a, np.ndarray): return False
    if len(np.shape(a)) != 2: return False
    if not isVec3( a[0] ) : return False
    return True

def assertIsArrayOfVec3( a : np.ndarray , context : str) -> None :
    assert isArrayOfVec3(a), context + ": elements of ndarray must be vec3, i.e. sub-arrays with shape (3,)"

def isScalarArrayOfDoubles( a: np.ndarray) -> bool:
    if not isinstance(a, np.ndarray): return False
    if len(np.shape(a)) != 1: return False
    if a.dtype != np.double(999).dtype: return False
    return True

# tentative argument prefix naming convention: ( PEP8 does not specify how to name variables & arguments )
# as_xxx : an array of scalars ( i.e. a 1-dim array )
# av_xxx : an array of vectors ( i.e. a generic 2-dim array )
# av3_xxx: an array of vec3's
# v3_xxx: a vec3 ( i.e. a 1-dim array of length 3 )

class TimeSeries:

    # self.t is an array of doubles ; i.e. t[i] is the i-th t-value
    # todo: store self.delta_t, an array of doubles ( more efficient for core computations )
    # todo: provide self.getTArray() ( used mostly by plot utilities )

    def __init__(self, as_t):
        assert (isScalarArrayOfDoubles(as_t))
        self.t = as_t

    def __len__(self) -> int:
        return len(self.t)

class AccelData (TimeSeries):

    # self.a is an array of vec3's  ; i.e. a[i] is an array of length 3 holding the acceleration vector at time t[i]
    # ( this is the opposite of the current AccelData, in which a[i] is an array of length n holding
    # the values of the i-th component of the acceleration vector for all time steps.
    # i.e. old layout : a[axis][time]
    #      new layout : a[time][axis]

    def __init__(self, as_t, av3_a, sModelType = "unspecified model type"  ):

        TimeSeries.__init__(self,as_t)

        assertIsArrayOfVec3(av3_a, context = "Accel constructor")
        ff = len(av3_a)
        jj = len(as_t)
        assert len(av3_a) == len(as_t) , "accel raw data not same length as time values"
        self.a = av3_a

        self.model = sModelType


    def getSingleAxis(self, axisIndex):
        return self.a[:,axisIndex]


class RotaryData (TimeSeries):

    def __init__(self, as_t, as_omega):

        TimeSeries.__init__(self,as_t)

        assert isScalarArrayOfDoubles(as_omega), "RotaryData constructor"
        assert( len(as_omega)==len(self))
        self.omega = as_omega


################ test ################

def test_DataStructures() -> None:

    v3_good = np.ndarray(shape=(3,), dtype=np.double)
    v3_bad1 = np.ndarray(shape=(2,), dtype=np.double)
    v3_bad2 = np.ndarray(shape=(3,2), dtype=np.double)
    v3_bad3 = np.ndarray(shape=(10,3), dtype=np.double)
    v3_bad4 = np.ndarray(shape=(3,), dtype=np.int)

    assert(isVec3(v3_good))
    assert(not isVec3(v3_bad1))
    assert(not isVec3(v3_bad2))
    assert(not isVec3(v3_bad3))
    assert(not isVec3(v3_bad4))

    av3_good = np.ndarray(shape=(10,3), dtype=np.double)
    av3_bad1 =np.ndarray(shape=(3,), dtype=np.double)
    av3_bad2 =np.ndarray(shape=(10,4), dtype=np.double)
    av3_bad3 = list([[1,2,3],[4,5,6]])

    assert(isArrayOfVec3(av3_good))
    assert(not isArrayOfVec3(av3_bad1))
    assert(not isArrayOfVec3(av3_bad2))
    assert(not isArrayOfVec3(av3_bad3))


    t = np.ndarray(shape=(10,), dtype=np.double)
    ad = AccelData(t,av3_good)

    t_bad = np.ndarray(shape=(9,), dtype=np.double)

    av3_good[0] = [1,2,3]
    av3_good[1] = [4,5,6]
    av3_good[2] = [7,8,9]
    xValues = ad.getSingleAxis(axisIndex=0)
    print('x values ', xValues[:3])
    xValues = ad.getSingleAxis(axisIndex=2)
    print('z values ', xValues[:3])

if __name__ == "__main__" : test_DataStructures()
