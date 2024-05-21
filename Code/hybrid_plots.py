import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import physical_constants

def hybridise_wavefunctions(r, orb_type):
    """
    Create hybrised orbital based on the percentage character of s and p orbitals
    """
    #Calculates the s and p radial wavefunction over radii given
    s_r = radial_wavefunction(2, 0, r)
    p_r = radial_wavefunction(2, 1, r)
    if orb_type == "s_p":
        #Calculates s and p character based on percentage in hydrised orbital
        #Converts radial wavefunction to distribution function
        s_r = 0.5 * (4 * np.pi * r**2 * np.abs(s_r)**2)
        p_r = 0.5 * (4 * np.pi * r**2 * np.abs(p_r)**2)
    elif orb_type == "s_p_2":
        s_r = 0.33 * (4 * np.pi * r**2 * np.abs(s_r)**2)
        p_r = 0.66 * (4 * np.pi * r**2 * np.abs(p_r)**2)
    elif orb_type == "s_p_3":
        s_r = 0.25 * (4 * np.pi * r**2 * np.abs(s_r)**2)
        p_r = 0.75 * (4 * np.pi * r**2 * np.abs(p_r)**2)
    return s_r, p_r #returns s and p distrbutions

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
 

def hybrid_plot_orbitals(orb_type, r_min, r_max, plot_type):
    """
    Plots the radial distribution function of hybrised orbitals dependant on the user's input, plot_type
    """
    if plot_type == '1D':
        #Creates range of radii to use 
        r = np.linspace(r_min, r_max, 400)
        #Calculates the radial distrubtion of s and p obrital character
        s_R, p_R = hybridise_wavefunctions(r, orb_type)
        #Adds raidal distributions together
        R = np.sum([s_R, p_R], axis = 0)
        
        #Plots graph including title and axis labels
        plt.figure(figsize=(8, 4))
        plt.plot(r, R**2, linewidth=2)
        plt.title(f'Radial Probability Distribution: {orb_type} Orbital')
        plt.xlabel('Radius (angstroms)')
        plt.ylabel('Probability Density')
        plt.grid(True)
        
    elif plot_type == '2D':
        #Generates a range of radii in a both x and y axis
        x = np.linspace(-r_max, r_max, 400)
        y = np.linspace(-r_max, r_max, 400)
        X, Y = np.meshgrid(x, y)
        #creates radii used in radial wavefunction
        r = np.sqrt(2*X**2 +2*Y**2)
        #calculates the radial distrubition function 
        s_R, p_R = hybridise_wavefunctions(r, orb_type)
        Z = np.sum([s_R, p_R * X / r], axis = 0)
    
        #Plots contour graph including title and axis title
        plt.figure(figsize=(8, 8))
        plt.pcolormesh(X, Y, Z**2, shading='auto', cmap='inferno')
        plt.title(f'Orbital Shape in 2D: {orb_type} Orbital')
        plt.xlabel('X (angstroms)')
        plt.ylabel('Y (angstroms)')
        plt.axis('scaled')
        plt.colorbar(label='Probability Density')
        plt.xlim(-2,2)
        plt.ylim(-2,2)
    #Returns plot
    return plt