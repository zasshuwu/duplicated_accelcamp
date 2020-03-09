#---------------------
# Class and functions for kinematic analysis
# -of a single acceleration time step ( class Cell )
# -of neighbouring time steps ( class Cluster )
#-----------------------

from modules.DataStructures import *

# acceleration data and associated operations
# for a single time step
# does NOT include radius as a permanent member:
# the radius is always treated as a trial or inferred value.
class Cell:

    def __init__(self, ar: float, at: float, delta_t: float):
        self.ar = ar
        self.at = at
        self.delta_t = delta_t

    # angle of total acceleration angle from radial direction
    def accelAngle(self):
        return 180/np.pi * np.arctan(-self.ar/self.at)


    #---------------------------
    # functions relying on a trial value for radius
    #---------------------------
    def v_UsingRadius(self, radius: float):
        return np.sqrt(self.ar * radius)

    def v_next_PredictedUsingRadius(self, radius: float):
        return self.v_UsingRadius(radius) + self.at * self.delta_t

    def ar_next_PredictedUsingRadius(self, radius : float):
        return np.square(self.v_next_PredictedUsingRadius(radius))/radius

    def ar_dot_PredictedUsingRadius(self, radius: float):
        return (self.ar_next_PredictedUsingRadius(radius) - self.ar)/self.delta_t

    def ar_dot_PredictedUsingRadius_alt(self, radius: float ):
        term1 = np.square(self.at) / radius * self.delta_t
        term2 = 2 * self.at * np.sqrt(self.ar / radius)
        return term1 + term2


# acceleration data and associated operations
# for two neighbouring time steps
# does NOT include radius as a permanent member:
# the radius is always treated as a trial or inferred value.
class Cluster:
    def __init__(self):
        self.cell = np.NAN
        self.ar_next = np.NAN


    def setFromAccelData(self, ad : AccelData):
        self.cell = Cell(ad.a[i][0],ad.a[i][1],ad.delta_t())
        self.ar_next = ad.a[i+1][0]

    # This calc does NOT require any radius value;
    # it is based on the actual data for ar_next
    def ar_dot(self):
        return (self.ar_next - self.cell.ar)/self.cell.delta_t


    # ---------------------------
    # functions relying on a trial value for radius
    # ---------------------------

    # distinct from Cell:v_next_UsingRadius()
    # this one uses the actual data ar_next
    # the other one predicts ideal ar_next based on radius

    def v_next_UsingRadius(self, radius: float):
        return np.sqrt(self.ar_next * radius)

    def delta_v_UsingRadius(self, radius: float):
        return self.v_next_UsingRadius(radius)-self.cell.v_UsingRadius(radius)

    def delta_v_over_v(self, radius: float):
        return self.delta_v_UsingRadius(radius)/self.cell.v_UsingRadius(radius)


    def signed_cost(self, radius : float):
        return self.ar_dot() - self.cell.ar_dot_PredictedUsingRadius(radius)
        # checking that compact expression ( "alt" ) produces same result
        # return self.ar_dot() - self.cell.ar_dot_UsingRadius_alt(radius)

    def cost(self, trialRadius):
        if ( trialRadius < 0.0):
            return 1.0
        return np.square(self.signed_cost(trialRadius))

    # this implementation is a deliberate copy of the one in tfPhysics
    # cost_SimpleRadial()
    def cost2(self, trialRadius: float ):
        term1 = np.square(self.cell.at) * self.cell.delta_t
        term2 = 2 * self.cell.at * np.sqrt(self.cell.ar*trialRadius)
        return np.square(self.ar_dot() - term1 + term2)

    def term1(self , trialRadius: float):
        return np.square(self.cell.at) * self.cell.delta_t

    def term2(self, trialRadius: float):
        return 2 * self.cell.at * np.sqrt(self.cell.ar*trialRadius)

    def costDeltaV(self, trialRadius: float):
        deltaV1 = self.cell.at * self.cell.delta_t
        v_initial = np.sqrt(trialRadius* self.cell.ar)
        v_final = np.sqrt(trialRadius* self.ar_next)
        deltaV2 = v_final - v_initial
        return np.square(deltaV1-deltaV2)



# global class functions
# ( because python forbids overloading of constructors )

def Cluster_CreateFromCellAndFloat( cell : Cell, ar_next : float ):
    cluster = Cluster()
    cluster.cell = cell
    cluster.ar_next = ar_next
    return cluster

def Cluster_CreateFromCell( cell : Cell, radius: float ):
    return Cluster_CreateFromCellAndFloat( cell, cell.ar_next_PredictedUsingRadius(radius))

def Cluster_CreateFromAccelData( ad : AccelData, i : int):
    cell = Cell(ad.a[i][0],ad.a[i][1],ad.delta_t(i))
    return Cluster_CreateFromCell(cell,ad.a[i+1][0])

def AccelData_CreateFromRotary_Tmp( rotData : RotaryData, radius : float):
    #a = np.ndarray( len(rotData), 3 )

    a = np.ndarray(shape=(len(rotData),3), dtype=np.double)
    omega = rotData.omega
    for i in range(len(omega) - 1):
        a[i][0] = np.square(omega[i])*radius
        a[i][1] = radius * ( omega[i+1]-omega[i])/( rotData.delta_t(i))
        a[i][2]=0

    return AccelData( rotData.t, a, "new simulated data")

def AccelData_Debug( ad: AccelData, rd : RotaryData):
    for i in range(len(rd)-2):
        omega = rd.omega[i]
        omegaNext = rd.omega[i+1]
        cl = Cluster_CreateFromAccelData(ad,i)




    return