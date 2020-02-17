import itertools
import numpy
force = [[6.62956956, -8.577826087],[5.832021531, -9.304479904],[5.54374, -8.92928],[4.788803883, -8.765187379],[3.874473786, -9.243305825],[3.4989, -8.687922857],[2.821763208, -8.963193396],[2.229205714, -9.193371429],[1.415306796, -8.829952427],[0.860477143, -9.218597143]]
r = [[-25/2,14],[-25/2,14]]
positions = []
xList = []
yList = []
average  = [0, 0]

for i in range(len(force)) :
    force[i].append(r[0][0])
    force[i].append(r[1][0])
    r[0][0] += 1
    r[1][0] += 1

def FindPosition(F):
    a = -F[0][1]
    b = F[0][0]
    c = (F[0][1] * F[0][2]) - (F[0][0] * F[0][3])
    d = -F[1][1]
    e = F[1][0]
    f = (F[1][1] * F[1][2]) - (F[1][0] * F[1][3])
    x = [0, 0]
    x[1] = (f - ((c * d)/a))/(e - ((b * d)/a))
    x[0] = (c/a) - ((b/c) * x[1])
    positions.append(x)

for i in list(itertools.permutations(force, 2)):
    FindPosition(i)
    r[0][0] += 1
    r[1][0] += 1
for i in range(len(positions)):
    xList.append(positions[i][0])
    yList.append(positions[i][1])

average[0] = numpy.mean(xList)
average[1] = numpy.mean(yList)
print(average)