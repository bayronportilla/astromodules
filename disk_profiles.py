############################################################
#
# Some random scripts, but they could be useful someday 
#
# @bayronportilla-2019
#
############################################################

import numpy as np
import matplotlib.pyplot as plt
import sys
from astropy import constants as cte

kb=1.38e-23
mh=1.67e-27
mu=2.3
M=0.8*1.989e30
G=6.67e-11

class chiang_goldreich:
    def __init__(self,r):
        self.r=r
    def T_dust_surface(r):
        value=550.0*r**(-2./5) # (K)
        return value
    def T_interior(self):
        try:
            if 270.0<r<0.4:
                raise ValueError('outside limits')
            if 0.4<=r<84.0:
                value=150.0*r**(-3./7)
                return value
            elif 84<=r<209.0:
                value=21.0
                return value
            elif 209.0<=r<=270.0:
                value=200.0*r**(-19./45)
                return value
        except ValueError:
            print ("nop")
        
def asd():
    return 0
sys.exit()
def T(r):
    if 0.4<=r<=84:
        value=150*r**(-3/7.)
    elif 84<r<=209:
        value=21.
    elif 209<r<=270:
        value=200.4*r**(-19/45)
    return value

def cs(r):
    value=(kb*T(r)/(mu*mh))**0.5
    return value
    
def Omega(r):
    value=(G*M/r**3)**0.5
    return value
        
def h(r):
    value=cs(r)/Omega(r)
    return value
    

d=np.linspace(0.4,20,100)
h_array=[]

for i in d:
    h_array.append(h(i))


plt.plot(d,h_array)
plt.show()

