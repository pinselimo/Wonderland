# Welcome to Wonderland

This package comprises the Wonderland model as proposed by Sanderson (1992) and published by Milik et al. (1996).

## Installation

Installing the Python-Wonderland in your environment works with pip. Once you are in this directory execute:

~~~bash
pip install .
~~~

### Requirements

To install only requirements, open a shell in this directory under your Python environment and execute:

~~~bash
pip install -r requirements.txt
~~~

## Scenarios

For trying out the different proposed scenarios, start a Python shell in this directory and execute:

~~~python
import wonderland as wl
wl.plot_xzp(wl.Szenario(wl.Wonderland(wl.horror_parameter)))
~~~

This will give you the *Environmentalist's Nightmare Scenario*. To switch to the *Economist's Dream Scenario*:

~~~python
wl.plot_xzp(wl.Szenario(wl.Wonderland(wl.dream_parameter)))
~~~

## Testing

To run the tests from this directory, open a shell in the environment you previously installed the requirements, then execute:

~~~bash
pytest tests/tests.py
~~~

**Sources**
[Sanderson, W.C. (1992). Simulation Models of Economic, Demographic, and Environmental Interactions: Are They on a Sustainable Development Path?. Laxenburg: International Institute for Applied Systems Analysis.](http://pure.iiasa.ac.at/id/eprint/3613/)

[Milik, A., Prskawetz, A., Feichtinger, G. & Sanderson, W.C. (1996). Slow-fast dynamics in Wonderland. Environmental Modeling and Assessment, 1 (2), S. 3–17](http://pure.iiasa.ac.at/id/eprint/4854/)
