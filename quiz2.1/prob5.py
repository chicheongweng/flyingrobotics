import numpy as np
import math

def sm(v):
    a = v[0]
    b = v[1]
    c = v[2]
    return np.matrix([[0, -c, b],[c, 0, -a],[b, a, 0]])

def sqrt(x):
    return math.sqrt(float(x))

R = np.matrix([[-1.0/3, 2.0/3, -2.0/3],[2.0/3, -1.0/3, -2.0/3],[-2.0/3, -2.0/3, -1.0/3]])
#print R*R.transpose()

u = [-0.9066, 0.9066, 0.9066]
phi = 0.2
print sm(u) - (R - R.transpose())/2/math.sin(phi)

u = [-0.9066, -0.9066, -0.9066]
phi = 3.14159
print sm(u) - (R - R.transpose())/2/math.sin(phi)

u = [sqrt(3)/3.0, sqrt(3)/3.0, -sqrt(3)/3.0]
phi = 3.14159
print sm(u) - (R - R.transpose())/2/math.sin(phi)

u = [-sqrt(3)/3.0, sqrt(3)/3.0, -sqrt(3)/3.0]
phi = 0.2
print sm(u) - (R - R.transpose())/2/math.sin(phi)

