#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

quantum_system = QuantumSystem(x_initial=0, x_final=1, num_points=1000, potential=potential_function)
energies, wavefunctions = quantum_system.solve()

# normalize
normalized_wavefunctions = quantum_system.normalize_wavefunctions(wavefunctions)
quantum_system.plot_wavefunctions(normalized_wavefunctions/2)

potential = Potential()
solver = WaveFunctionSolver(potential)
simulation = MonteCarloSimulation(solver)
simulation.run()
