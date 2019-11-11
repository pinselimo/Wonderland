# -*- coding: utf-8 -*-
from .core import population, wirtschaft, technologie, umwelt

x_0 = y_0 = p_0 = 1.0
z_0 = 0.98

def simulation(jahre=250):
    ergebnis = [(x_0,y_0,z_0,p_0)]
    for jahr in range(1,jahre):
        x, y, z, p = ergebnis[jahr-1]
        x_neu = population(x,y,z)
        y_neu = wirtschaft(y,z)
        z_neu = umwelt(x,y,z,p)
        p_neu = technologie(p)
        ergebnis.append((x_neu, y_neu, z_neu, p_neu))
    return ergebnis