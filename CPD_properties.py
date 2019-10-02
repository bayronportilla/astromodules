import numpy as np
from astropy import constants as cte

def hill_radius(M,m,a,e):

    ############################################################
    #
    # Computes the Hill radius around a planet of mass m 
    # moving around star M in an orbit with semi-major axis
    # a and eccentricity e. Units of the output are the 
    # same units of the semi-major axis.
    #
    ############################################################

    value=a*(1-e)*(m/(3*M))**(1./3)
    return value
