from context import Wonderland, scenarios, parameters

import py.test
from hypothesis import given
import hypothesis.strategies as strat

st_z = strat.floats(min_value=0.0,max_value=1.0,allow_nan=False)
st_p = strat.floats(min_value=0.0,max_value=1.0,allow_nan=False,exclude_min=True)
st_x = strat.floats(min_value=0.0,max_value=10.0,allow_nan=False,allow_infinity=False)
st_y = strat.floats(min_value=0.0,max_value=1000.0,allow_nan=False,allow_infinity=False)

PS = parameters.dream_parameters

@given(st_p)
def teste_technologie_im_definitionsbereich(p):
    res = Wonderland(PS).technologie(p)
    assert res >= 0 and res <= 1

@given(st_y, st_z)
def teste_wirtschaft_im_definitionsbereich(y,z):
    res = Wonderland(PS).wirtschaft(y,z)
    assert res >= 0
    
@given(st_x, st_y, st_z)
def teste_population_im_definitionsbereich(x,y,z):
    res = Wonderland(PS).population(x,y,z)
    assert res >= 0
    
@given(st_y, st_z)
def teste_geburtenrate_positiv(y,z):
    res = Wonderland(PS).geburtenrate(y,z)
    assert res >= 0

@given(st_y, st_z)
def teste_sterberate_positiv(y,z):
    res = Wonderland(PS).sterberate(y,z)
    assert res >= 0
    
@given(st_y, st_z)
def teste_netto_produktion_minimal_halbe_wirtschaftsleistung(y,z):
    res = y - Wonderland(PS).umweltschutz(y,z)
    assert res >= y/2
    
@given(st_y, st_z)
def teste_umweltschutzausgaben_unter_wirtschaftsleistung(y,z):
    res = Wonderland(PS).umweltschutz(y,z)
    assert res <= y and res >= 0
    
@given(st_x, st_y, st_z)
def teste_fluss_umweltverschmutzungen_in_simulationsdauer_positiv(x,y,z):
    p = 1.0
    for _ in range(500):
        p = Wonderland(PS).technologie(p)
        
    res = Wonderland(PS).fluss_emissionen(x,y,z,p)
    assert res >= 0
    
@given(st_x, st_y, st_z)
def teste_umweltzustand_im_definitionsbereich(x,y,z):
    p = 1.0
    for _ in range(500):
        p = Wonderland(PS).technologie(p)

    res = Wonderland(PS).umwelt(x,y,z,p)
    assert res >= 0 and res <= 1
    
    