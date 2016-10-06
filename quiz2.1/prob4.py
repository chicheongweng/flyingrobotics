import numpy as np
import math

def sm(v):
    a = v[0]
    b = v[1]
    c = v[2]
    return np.matrix([[0, -c, b],[c, 0, -a],[b, a, 0]])

def sqrt(x):
    return math.sqrt(float(x))

R = np.matrix([[0.2919, 0.643, -0.7081],[-0.643, -0.4161, -0.643],[-0.7081, 0.643, 0.2919]])

u = [1/sqrt(2), -1/sqrt(2), 0]
phi = 0.8
print sm(u) - (R - R.transpose())/2/math.sin(phi)
print math.cos(phi), (R.trace()-1)/2.0

u = [-1/sqrt(2), 0, 1/sqrt(2)]
phi = 2
print sm(u) - (R - R.transpose())/2/math.sin(phi)
print math.cos(phi), (R.trace()-1)/2.0

u = [-1/sqrt(2), 0, 1/sqrt(2)]
phi = 0.8
print sm(u) - (R - R.transpose())/2/math.sin(phi)
print math.cos(phi), (R.trace()-1)/2.0

u = [1/sqrt(2), 0, -1/sqrt(2)]
phi = 2
print sm(u) - (R - R.transpose())/2/math.sin(phi)
print math.cos(phi), (R.trace()-1)/2.0

