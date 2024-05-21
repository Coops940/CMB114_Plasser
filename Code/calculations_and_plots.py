#JACK'S CODE
#imports all libraries used
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import physical_constants

def radial_wavefunction(n, l, r):
    """
    Function used to caluate the radial wvafunciton dependant on n, l of orbital and rnage of radii given.
    """
    a0 = physical_constants['Bohr radius'][0] * 1e10  # Convert Bohr radius to angstroms
    Z = 1  # Assume Z=1 for hydrogen-like orbitals in a water molecule approximation
    #Compares n and l to identify the equation to use
    if n == 1 and l == 0:  # 1s
        return 2 * (Z/a0)**1.5 * np.exp(-Z * r / a0)
    elif n == 2 and l == 0:  # 2s
        return (1/4*np.sqrt(2)) * (Z/2/a0)**1.5 * (2 - Z*r/a0) * np.exp(-Z*r/(2*a0))
    elif n == 2 and l == 1:  # 2p
        return (1/(2*np.sqrt(6))) * (Z/2/a0)**1.5 * (Z*r/a0) * np.exp(-Z*r/(2*a0))
    return np.zeros_like(r)

def plot_orbitals(n, l, r_min, r_max, plot_type):
    """
    Plots the radial distribution function dependant on the user's input, plot_type
    """
    #Checks to see if the plot_type is 1D
    if plot_type == '1D':
        #Generates a range of radii 
        r = np.linspace(r_min, r_max, 400)
        #Calculates radial wavefunction over range of radii
        R = radial_wavefunction(n, l, r)
        R = 4 * np.pi * r**2 * np.abs(R)**2 #Changes radial wavefunction to radial distrbution function
        
        #Creates plot with title and axis labels
        plt.figure(figsize=(8, 4))
        plt.plot(r, R**2, label=f'n={n}, l={l}', linewidth=2)
        plt.title(f'Radial Probability Distribution: {n}{["s", "p"][l]} Orbital')
        plt.xlabel('Radius (angstroms)')
        plt.ylabel('Probability Density')
        plt.legend()
        plt.grid(True)
    #Checks to see if the plot_type is 2D
    elif plot_type == '2D':
        #Generates a range of radii in a both x and y axis
        x = np.linspace(-r_max, r_max, 400)
        y = np.linspace(-r_max, r_max, 400)
        #Creates grid
        X, Y = np.meshgrid(x, y)
        #creates radii used in radial wavefunction
        r = np.sqrt(2*X**2 + 2*Y**2)
        if l == 0:
            #calculates the radial distrubition function 
            Z = 4 * np.pi * r**2 * np.abs(radial_wavefunction(n, l, r))**2
        elif l == 1:
            Z = 4 * np.pi * r**2 * np.abs(radial_wavefunction(n, l, r))**2 * X / r
        
        #Creates contour plot with title and axis labels
        plt.figure(figsize=(8, 8))
        plt.pcolormesh(X, Y, Z**2, shading='auto', cmap='inferno')
        plt.title(f'Orbital Shape in 2D: {n}{["s", "p"][l]} Orbital')
        plt.xlabel('X (angstroms)')
        plt.ylabel('Y (angstroms)')
        plt.axis('scaled')
        plt.colorbar(label='Probability Density')
        plt.xlim(-2,2)
        plt.ylim(-2,2)
    return plt
