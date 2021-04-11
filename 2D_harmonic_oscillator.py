import numpy as np
from qmsolve import Halmitonian, animate, dynamic_visualize, SingleParticle


#interaction potential
def harmonic_oscillator(particle):

	kx = 100 # measured in eV / (Å**2)
	ky = 100
	return 0.5 * kx * particle.x**2    +    0.5 * ky * particle.y**2



H = Halmitonian(particles = SingleParticle(), 
				potential = harmonic_oscillator, 
				spatial_ndim = 2, N = 200, extent = 15)


energies, eigenstates = H.solve(max_states = 30)

print(energies)
dynamic_visualize(energies, eigenstates)