import numpy as np
import matplotlib as plt
from pylab import *


def get_next_1(x, r):
  return sin(x)*r*(1-sin(x))

def get_next(x, r):
  return x*r*(1-x)

def get_equilibrium(n, x, r):

  for i in range(1,n):
    x = get_next(x, r)

  return x

seed = rand()       # Seed value for x in (0, 1)
iternum = 1000      # Number of iterations per point
res = 100             # Largest n-cycle visible - median filter
n_points = 20000    # n point in range [0,4]

# Initialize r and x lists
rlist = np.zeros(n_points)
xlist = np.zeros(n_points)

# Generate list values -- iterate for each value of r
r_range = np.linspace(0,4,n_points)#[i * spacing for i in range(start_r,stop_r)]
this_p = 0
for r in r_range:
  rlist[this_p] = r
  xlist[this_p] = get_equilibrium(iternum+int((rand()*10)%10), seed, r)
  this_p +=1

scatter(rlist, xlist, s = .01)
xlim(3.5, 4.1)
ylim(-0.1,1.1)
show()
