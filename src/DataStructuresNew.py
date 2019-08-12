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

    def __init__(self, as_t):
        assert (isScalarArrayOfDoubles(as_t))
        self.t = as_t

    def len(self) -> int:
        return len(self.t)

class AccelTS (TimeSeries):

    # self.a is an array of vec3's  ; i.e. a[i] is an array of length 3 holding the acceleration vector at time t[i]
    # ( this is the opposite of the current AccelData, in which a[i] is an array of length n holding
    # the values of the i-th component of the acceleration vector for all time steps.

    def __init__(self, as_t, av3_a  ) -> None :

        TimeSeries.__init__(self,as_t)

        assertIsArrayOfVec3(av3_a, context = "Accel constructor")
        self.a = av3_a

        self.model = "unspecified sensor model"

    def len(self)-> int:
        return len(self.t)

class RotaryTS (TimeSeries):

    def __init__(self, as_t, av3_omega):

        TimeSeries.__init__(self,as_t)

        assertIsArrayOfVec3(av3_omega, context="RotaryData constructor")
        assert( len(av3_omega)==self.len() )
        self.omega = av3_omega


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
    ad = AccelTS(t,av3_good)
    rd = RotaryTS(t,av3_good)

    t_bad = np.ndarray(shape=(9,), dtype=np.double)

if __name__ == "__main__" : test_DataStructures()
