from collections.abc import Sequence

class ZustandsSammlung(Sequence):
    """Sammlung der Zustände einer Wonderland-Simulation

    :param wonderland: core.Wonderland
    """
    def __init__(self,wonderland):
        self._zustände = list()
        self._zustände.append(wonderland.zustand)
        self._PS = wonderland.PARAMETER

    def __len__(self):
        return len(self._zustände)

    def __getitem__(self, index):
        return self._zustände[index]

    def speichere(self, neuer_zustand):
        """Fügt einen neuen Zustand zur Sammlung hinzu.

        :param neues_wonderland: core.WonderlandZustand
        """
        self._zustände.append(neuer_zustand)
        return None

class Szenario:
    """Führt eine Simulation basierend auf einem
    Wonderland aus.

    :param wonderland: core.Wonderland
    :param jahre: int, Simulationsperiode
    """
    def __init__(self, wonderland, jahre=300):
        """Standarddauer einer Simulationsperiode: 300 Jahre
        """
        self._wonderland = wonderland
        self._ergebnis = ZustandsSammlung(self._wonderland)

        for _ in range(jahre):
            self._ergebnis.speichere(self._wonderland.neues_jahr())

    @property
    def wonderland(self):
        """Gibt das hinterlegte Wonderland aus.
        """
        return self._wonderland

    @property
    def ergebnis(self):
        """Gibt das berechnete Ergebnis aus.
        """
        return self._ergebnis