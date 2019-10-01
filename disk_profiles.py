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

class Chiang_Goldreich:
    def __init__(self,r):
        self.r=r
    def T_dust_surface(self):
        try:
            if self.r>270.0 or self.r<0.4:
                raise ValueError
            else:
                value=550.0*self.r**(-2./5) 
                return value
        except ValueError:
            print('r is outside the limits of Chiang-Goldreich model')
    def T_interior(self):
        try:
            if self.r>270.0 or self.r<0.4:
                raise ValueError
            elif 0.4<=self.r<84.0:
                value=150.0*self.r**(-3./7)
                return value
            elif 84<=self.r<209.0:
                value=21.0
                return value
            elif 209.0<=self.r<=270.0:
                value=200.0*self.r**(-19./45)
                return value
        except ValueError:
            print('r is outside the limits of Chiang-Goldreich model') 
    def h_scale(self):
        try:
            if self.r>270.0 or self.r<0.4:
                raise ValueError
            elif 0.4<=self.r<84.0:
                value=0.17*self.r**(2./7)*r
                return value
            elif 84<=self.r<209.0:
                value=0.064*r**0.5*r
                return value
            elif 209.0<=self.r<=270.0:
                value=0.2*self.r**(13./45)*r
                return value
        except ValueError:
            print('r is outside the limits of Chiang-Goldreich model') 
    
"""
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

"""
