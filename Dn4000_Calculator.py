"""
Dn4000 Calculator

Author: George Ridgeway <george_ridgeway@outlook.com>
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.constants import c

# Define wavelength ranges in angstroms:
upper_higher_wave = 4100
upper_lower_wave = 4000
lower_higher_wave = 3950
lower_lower_wave = 3850

# If mask is available, mask flux,wavelength, and variance before

def dn4000_calculate(flux,wavelength,variance,redshift,plot=True,redshifted=True):
    
    c = (scipy.constants.c)*10**10  #[angstrom/s]
    
# Shift spectrum to rest frame wavelengths
    if redshifted == True: 
        rest_frame_wavelength = wavelength

    if redshifted == False: 
        rest_frame_wavelength = ((wavelength)/(redshift+1))
        
# Select wavelengths between lower_lower_wave and upper_higher_wave

    dn4000_range = (rest_frame_wavelength > lower_lower_wave) & (rest_frame_wavelength < upper_higher_wave)
    
    rest_frame_wavelength_dn4000 = rest_frame_wavelength[dn4000_range]
    flux_dn4000 = flux[dn4000_range]
    variance_dn4000 = variance[dn4000_range]
    
# Find average frequency flux density in blue(3850-3950) and red wavelenghts(4000-4100)
# flux density frequency = (c/frequency**2)*(flux density wavelength)

    upper_dn4000_range = (rest_frame_wavelength_dn4000 > upper_lower_wave) & (rest_frame_wavelength_dn4000 < upper_higher_wave)
    upper_wavelength_dn4000 = rest_frame_wavelength_dn4000[upper_dn4000_range]
    upper_frequency_dn4000 = (c/upper_wavelength_dn4000)
    
    flux_conversion_upper = (c/(upper_frequency_dn4000**2))
    
    upper_flux_wavelength_dn4000 = flux_dn4000[upper_dn4000_range]
    
    upper_flux_dn4000 = (flux_dn4000[upper_dn4000_range])*flux_conversion_upper
    upper_variance_dn400 = variance_dn4000[upper_dn4000_range]
    upper_flux_dn4000_average = np.average(upper_flux_dn4000)
    
    lower_dn4000_range = (rest_frame_wavelength_dn4000 > lower_lower_wave) & (rest_frame_wavelength_dn4000 < lower_higher_wave)
    lower_wavelength_dn4000 = rest_frame_wavelength_dn4000[lower_dn4000_range]
    lower_frequency_dn4000 = (c/lower_wavelength_dn4000)
    
    flux_conversion_lower = (c/(lower_frequency_dn4000**2))
    lower_flux_wavelength_dn4000 = flux_dn4000[lower_dn4000_range]
    lower_flux_dn4000 = (flux_dn4000[lower_dn4000_range])*flux_conversion_lower
    lower_variance_dn400 = variance_dn4000[lower_dn4000_range]
    lower_flux_dn4000_average = np.average(lower_flux_dn4000)
    
# Take ratio of upper and lower flux

    dn4000 = (upper_flux_dn4000_average)/(lower_flux_dn4000_average)
    
# Calculate error from variance

    std_upper = (1/(np.sqrt(upper_variance_dn400)))*flux_conversion_upper
    std_lower = (1/(np.sqrt(lower_variance_dn400)))*flux_conversion_lower
    
    sigma_upper = np.sqrt(np.sum(std_upper**2))/(len(upper_flux_dn4000))
    sigma_lower = np.sqrt(np.sum(std_lower**2))/(len(lower_flux_dn4000))
    
    std_dn4000 = np.sqrt(((((1/lower_flux_dn4000_average)*sigma_upper)**2) + (((upper_flux_dn4000_average/(-lower_flux_dn4000_average**2))*sigma_lower))**2))
    
# Diagnostic Plots

    if plot == True:
        
        plt.plot(rest_frame_wavelength,flux)
        plt.show()
        
        plt.plot(rest_frame_wavelength_dn4000,flux_dn4000)
        plt.title('Spectra from 3850-4100 adjusted for redshift')
        plt.xlabel('Wavelength')
        plt.ylabel('Counts (Flux)')
        plt.show()
        
        plt.plot(lower_wavelength_dn4000,lower_flux_wavelength_dn4000)
        plt.title('Spectra from 3850-3950 adjusted for redshift')
        plt.xlabel('Wavelength')
        plt.ylabel('Counts (Flux)')
        plt.show()
        
        plt.plot(upper_wavelength_dn4000,upper_flux_wavelength_dn4000)
        plt.title('Spectra from 4000-4100 adjusted for redshift')
        plt.xlabel('Wavelength')
        plt.ylabel('Counts (Flux)')
        plt.show()
    
    return print('Dn4000 = ', dn4000, '+/-', std_dn4000)
    
    
    
    
    
    
    
    
    
    
    
    
    
