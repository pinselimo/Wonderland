# -*- coding: utf-8 -*-
from .parameters import *
from math import exp

def technologie(p):
    return p*(1.0-CHI)

def wirtschaft(y,z):
    return y*(1.0+GAMMA-(GAMMA+ETA)*(1.0-z)**LAMBDA)

def population(x,y,z):
    return x*(1.0+geburtenrate(y,z)-sterberate(y,z))

def geburtenrate(y,z): 
    e = y_strich(BETA,y,z)
    return BETA1 * (BETA2 - e/(1.0+e))

def sterberate(y,z):
    e = y_strich(ALPHA,y,z)
    return DELTA1 * (DELTA2 - e/(1.0+e)) * (1.0 + DELTA3 * (1.0-z)**THETA)

def y_strich(CONST,y,z):
    return exp(CONST * (y - umweltschutz(y,z)))

def fluss_emissionen(x,y,z,p):
    c_strich = exp(EPSILON * umweltschutz(y,z) * x)
    return x*y*p - KAPPA * (c_strich/(1.0+c_strich) - 0.5)

def umweltschutz(y,z):
    return PHI * (1.0-z)**MY * y

def umwelt(x,y,z,p):
    g = exp(DELTA*z**RHO - OMEGA*fluss_emissionen(x,y,z,p))
    return z + NY * (z**2.0 + z*g - g*z**2 - z)