import collections.abc

class ParameterSet(collections.abc.Mapping):
    """Speichert die Parameter des Wonderlands.
    
    :param CHI: Parameter CHI (0.04 für Dream-, 0.01 für Horror-Scenario)
    :param parameter_dict: Restliche Parameter als Schlüsselworte in 
        GROSSBUCHSTABEN.
    """
    def __init__(self,*, CHI, **parameter_dict):
        self._PS = {
            # Steuer
            'TAU':0,
            # Technologie
            'CHI':CHI, 'CHI_0':CHI/2, 
            # Umweltschutz
            'PHI':0.5, 'MY': 2.0, 
            # Umwelt
            'KAPPA':2.0, 'EPSILON':0.02, 'DELTA':1.0, 'RHO':2.0, 'OMEGA':0.1, 'NY':1.0,
            # Wirtschaft
            'GAMMA':0.02, 'ETA':0.1, 'LAMBDA':2.0, 'GAMMA_0':0.5,
            # Sterberate
            'ALPHA':0.18, 'DELTA1':0.01, 'DELTA2':2.5, 'DELTA3':4.0, 'THETA':15.0,
            # Geburtenrate
            'BETA1':0.04, 'BETA2':1.375, 'BETA':0.16
        }

        for parameter in parameter_dict:
            self._PS[parameter] = parameter_dict[parameter]

    def __len__(self):
        return len(self._PS)

    def __getitem__(self, index):
        return self._PS[index]

    def __iter__(self):
        return iter(self._PS)                  

dream_parameters = ParameterSet(CHI=0.04)
horror_parameters = ParameterSet(CHI=0.01)