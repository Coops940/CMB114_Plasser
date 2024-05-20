import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import physical_constants

def radial_wavefunction(n, l, r):
    a0 = physical_constants['Bohr radius'][0] * 1e10  # Convert Bohr radius to angstroms
    Z = 1  # Assume Z=1 for hydrogen-like orbitals in a water molecule approximation
    
    if n == 1 and l == 0:  # 1s
        return 2 * (Z/a0)**1.5 * np.exp(-Z * r / a0)
    elif n == 2 and l == 0:  # 2s
        return (1/4*np.sqrt(2)) * (Z/2/a0)**1.5 * (2 - Z*r/a0) * np.exp(-Z*r/(2*a0))
    elif n == 2 and l == 1:  # 2p
        return (1/(2*np.sqrt(6))) * (Z/2/a0)**1.5 * (Z*r/a0) * np.exp(-Z*r/(2*a0))
    return np.zeros_like(r)

def plot_orbitals(n, l, r_min, r_max, plot_type):
    r = np.linspace(r_min, r_max, 400)
    R = radial_wavefunction(n, l, r)
    R = 4 * np.pi * r**2 * np.abs(R)**2 #Changes radial wavefunction to radial distrbution function
    
    if plot_type == '1D':
        plt.figure(figsize=(8, 4))
        plt.plot(r, R**2, label=f'n={n}, l={l}', linewidth=2)
        plt.title(f'Radial Probability Distribution: {n}{["s", "p"][l]} Orbital')
        plt.xlabel('Radius (angstroms)')
        plt.ylabel('Probability Density')
        plt.legend()
        plt.grid(True)
        #plt.show()
    elif plot_type == '2D':
        x = np.linspace(-r_max, r_max, 400)
        y = np.linspace(-r_max, r_max, 400)
        X, Y = np.meshgrid(x, y)
        r = np.sqrt(X**2 + Y**2)
        if l == 0:
            Z = radial_wavefunction(n, l, r)
        elif l == 1:
            Z = radial_wavefunction(n, l, r) * X / r

        plt.figure(figsize=(8, 8))
        plt.pcolormesh(X, Y, Z**2, shading='auto', cmap='inferno')
        plt.title(f'Orbital Shape in 2D: {n}{["s", "p"][l]} Orbital')
        plt.xlabel('X (angstroms)')
        plt.ylabel('Y (angstroms)')
        plt.axis('scaled')
        plt.colorbar(label='Probability Density')
        plt.xlim(-2,2)
        plt.ylim(-2,2)
        #plt.show()
    return plt


# Example usage to plot 1s, 2s, and 2p in 1D and 2D
#orb_type = "1_s"
#plot_type = '1D'
#n, l = (int(orb_type.split('_')[0]), 0 if 's' in orb_type.split('_')[1] else 1)
#print(f"Plotting {orb_type} in {plot_type} view")
#plot_orbitals(n=n, l=l, r_min=0, r_max=10, plot_type=plot_type)
