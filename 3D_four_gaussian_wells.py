import numpy as np
from qmsolve import Hamiltonian, SingleParticle, init_visualization


#interaction potential
def four_gaussian_wells(particle):
	𝜇 = 1.0
	σ = 0.5
	V = 700*(4-np.exp((-(particle.x)**2 -(particle.y-𝜇)**2 -(particle.z)**2 ) / (2*σ**2))
	-np.exp((-(particle.x-𝜇)**2 -(particle.y)**2 -(particle.z)**2 ) / (2*σ**2))
	-np.exp((-(particle.x+𝜇)**2 -(particle.y)**2 -(particle.z)**2 ) / (2*σ**2))
	-np.exp((-(particle.x)**2 -(particle.y+𝜇)**2-(particle.z)**2  ) / (2*σ**2)))
	return V



H = Hamiltonian(particles = SingleParticle(), 
				potential = four_gaussian_wells, 
				spatial_ndim = 3, N = 30, extent = 5)


eigenstates = H.solve(max_states = 50)
print(eigenstates.energies)

visualization = init_visualization(eigenstates)
visualization.plot_eigenstate(40, contrast_vals = [0.1, 0.25])
visualization.animate(contrast_vals = [0.1, 0.25])