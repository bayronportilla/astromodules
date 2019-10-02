############################################################
#
# Routine to compute the height scale as a function of the 
# stellar mass and radial distance. 
#
# @bayronportilla-2019
#
############################################################

from chiang_goldreich_model import T_interior
from astropy import constants as cte

def h_scale(m_s,r):

    ############################################################
    # m_s: stellar mass in solar masses
    # r: radial distance (star at origin) in AU
    # output: height scale in AU
    ############################################################

    try:
        if r>270.0 or r<0.4:
            raise ValueError
        else:
            c_s=(cte.k_B.value*T_interior(r)/(2.3*cte.m_p.value))**0.5 # Sound speed
            W=(cte.G.value*m_s*cte.M_sun.value/(r*cte.au.value)**3)**0.5 # Angular frequency
            value=(c_s/W)/cte.au.value
            return value    
    except ValueError:
        return('r outside Chiang-Goldreich model')
