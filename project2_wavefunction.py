#!/usr/bin/env python3

import numpy as np
import matplotlib as plt
from project2 import Potentiall
from project2 import WaveFunctionSolverr
from project2 import MonteCarloSimulationn

potential = Potentiall()
solver = WaveFunctionSolverr(potential)
simulation = MonteCarloSimulationn(solver)
simulation.run()
