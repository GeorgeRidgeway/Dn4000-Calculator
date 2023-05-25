#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:31:13 2023

@author: georgeridgeway
"""

from astroML.datasets import fetch_sdss_spectrum


# Single SDSS Spectrum
plate = 1615
mjd = 53166
fiber = 507

spec = fetch_sdss_spectrum(plate, mjd, fiber)

from Dn4000_Calculator import dn4000_calculate
 

print(dn4000_calculate(spec.spectrum,spec.wavelength(),spec.error,spec.z,plot=True,redshifted=False))