from math import exp
from collections import namedtuple

WonderlandZustand = namedtuple('WonderlandZustand', 'x y z p')

class Wonderland:
    """Objekte vom Typ Wonderland besitzen:
    
    :param zustand_beginn: Ihren *aktuellen* Zustand
    :param parameter_set: Ihre *konstanten* Parameter
    """
    def __init__(self, parameter_set, zustand_beginn=WonderlandZustand(x=1.0,y=1.0,z=0.98,p=1.0)):
        """Der default Ausgangszustand ist so in allen Papern Konvention.
        """
        self._PS = parameter_set
        self._zustand = zustand_beginn

    def neues_jahr(self):
        """Berechnet den Zustand des nächsten Jahres.

        :returns: neuer WonderlandZustand
        """
        x,y,z,p = self._zustand
        x_neu = self.population(x,y,z)
        y_neu = self.wirtschaft(y,z)
        z_neu = self.umwelt(x,y,z,p)
        p_neu = self.technologie(p)
        self._zustand = WonderlandZustand(x_neu,y_neu,z_neu,p_neu)
        return self._zustand

    @property
    def zustand(self):
        """Gibt den *variablen* Zustand des Wonderland-Objekts aus.
        """
        return self._zustand

    @property
    def PARAMETER(self):
        """Gibt die *konstanten* Parameter des Wonderland-Objekts aus.
        """
        return self._PS

    def technologie(self, p):
        """Berechnet die Technologie des nächsten Wonderland-Jahres.

        :param p: Aktuelle Technologie.
        """
        TAU = self._PS['TAU']
        return p*(1.0-self._PS['CHI']-self._PS['CHI_0']*TAU/(1+TAU))

    def wirtschaft(self, y,z):
        """Berechnet die Wirtschaft des nächsten Wonderland-Jahres.

        :param y: Aktuelle Wirtschaftsleistung
        :param z: Aktueller Umweltzustand
        """
        GAMMA = self._PS['GAMMA']
        TAU = self._PS['TAU']
        return y*(1.0+GAMMA-(GAMMA+self._PS['ETA']) \
            *(1.0-z)**self._PS['LAMBDA']-self._PS['GAMMA_0']*(TAU/(1-TAU)))

    def population(self,x,y,z):
        """Berechnet die Bevölkerung des nächsten Wonderland-Jahres.

        :param x: Aktuelle Bevölkerung
        :param y: Aktuelle Wirtschaftsleistung
        :param z: Aktueller Umweltzustand
        """
        return x*(1.0+self.geburtenrate(y,z)-self.sterberate(y,z))

    def geburtenrate(self,y,z):
        """Berechnet wie stark die Bevölkerung durch Geburten ansteigt.

        :param y: Aktuelle Wirtschaftsleistung
        :param z: Aktueller Umweltzustand
        """
        e = self.y_strich(self._PS['BETA'],y,z)
        return self._PS['BETA1'] * (self._PS['BETA2'] - e/(1.0+e))

    def sterberate(self,y,z):
        """Berechnet wie stark die Bevölkerung durch Tode sinkt.

        :param y: Aktuelle Wirtschaftsleistung
        :param z: Aktueller Umweltzustand
        """
        e = self.y_strich(self._PS['ALPHA'],y,z)
        return self._PS['DELTA1'] * (self._PS['DELTA2'] - e/(1.0+e)) * (1.0 + self._PS['DELTA3'] * (1.0-z)**self._PS['THETA'])

    def y_strich(self,CONST,y,z):
        """Dient als Hilfsfunktion.

        *Nicht* das $\bar{y}$ in der klassischen Definition! 

        :param y: Aktuelle Wirtschaftsleistung
        :param z: Aktueller Umweltzustand
        """
        return exp(CONST * (y - self.umweltschutz(y,z)))

    def umwelt(self,x,y,z,p):
        """Berechnet die Umweltqualität des nächsten Wonderland-Jahres.

        :param x: Aktuelle Bevölkerung
        :param y: Aktuelle Wirtschaftsleistung
        :param z: Aktueller Umweltzustand
        :param p: Aktuelle Technologie
        """
        NY = self._PS['NY']
        g = exp(self._PS['DELTA']*z**self._PS['RHO'] - self._PS['OMEGA']*self.fluss_emissionen(x,y,z,p))
        resultat = z + NY * z*g - NY * z * (1.0-z+z*g)
        if resultat > 1:
            resultat = 1.0
        elif resultat < 0:
            resultat = 0.0
        return resultat

    def fluss_emissionen(self,x,y,z,p):
        """Berechnet den Fluss an Emissionen welche in Wonderlands
        Umwelt einfließen.

        :param x: Aktuelle Bevölkerung
        :param y: Aktuelle Wirtschaftsleistung
        :param z: Aktueller Umweltzustand
        :param p: Aktuelle Technologie
        """
        c_strich = exp(self._PS['EPSILON'] * self.umweltschutz(y,z) * x)
        return x*y*p - self._PS['KAPPA'] * (c_strich/(1.0+c_strich) - 0.5)

    def umweltschutz(self,y,z):
        """Berechnet die Kosten welche der Umweltschutz im Wonderland verursacht.

        :param y: Aktuelle Wirtschaftsleistung
        :param z: Aktueller Umweltzustand
        """
        return self._PS['PHI'] * (1.0-z)**self._PS['MY'] * y