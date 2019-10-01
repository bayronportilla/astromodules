def T_dust_surface(r):
    try:
        if r>270.0 or r<0.4:
            raise ValueError
        else:
            value=550.0*r**(-2./5) 
            return value
    except:
        return('r outside Chiang-Goldreich model')

def T_interior(r):   
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

def h_scale(r):
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
