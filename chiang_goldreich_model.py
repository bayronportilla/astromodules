############################################################
#
# The Chiang-Goldreich model.
# Based enterily on:
# The Astrophysical Journal, Volume 490, Issue 1, pp. 368-376
#
# The following modules are only a first approximation to 
# the quantities computed. In fact, these analytical relations 
# are only valid inside a narrow zone of the parameter space.
# In particular, they were derived for a disk surronding a 
# 0.5 solar mass star with a radius 2.5 that of the sun. 
# Also the effective temperature of the central star was 
# considered equal to 4000 K. The surface density of the 
# disk scales as r^-1.5. 
#
# @bayronportilla-2019
#
############################################################


def T_dust_surface(r):

    ############################################################
    #
    # Dust temperature in the disk surface. The input is the
    # distance to the central star in AU and the output is the 
    # temperature in K.
    #
    ############################################################

    try:
        if r>270.0 or r<0.4:
            raise ValueError
        else:
            value=550.0*r**(-2./5) 
            return value
    except ValueError:
        return('r outside Chiang-Goldreich model')


def T_interior(r):   

    ############################################################
    #
    # Temperature of the disk midplane. The input is the
    # distance to the central star in AU and the output is the 
    # temperature in K.
    #
    ############################################################

    try:
        if r>270.0 or r<0.4:
            raise ValueError
        elif 0.4<=r<84.0:
            value=150.0*r**(-3./7)
            return value
        elif 84<=r<209.0:
            value=21.0
            return value
        elif 209.0<=r<=270.0:
            value=200.0*r**(-19./45)
            return value
    except ValueError:
        return('r outside Chiang-Goldreich model')


def h_p(r):

    ############################################################
    #
    # Height of the visible photosphere. The input is the
    # distance to the central star in AU and the output is the 
    # AU.
    #
    ############################################################

    try:
        if r>270.0 or r<0.4:
            raise ValueError
        elif 0.4<=r<84.0:
            value=0.17*r**(2./7)*r
            return value
        elif 84<=r<209.0:
            value=0.064*r**0.5*r
            return value
        elif 209.0<=r<=270.0:
            value=0.2*r**(13./45)*r
            return value
    except ValueError:
        print('r is outside the limits of Chiang-Goldreich model') 
