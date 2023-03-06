import numpy as np
from eazy.filters import FilterFile
from astropy.cosmology import Planck18
import astropy.units as u
import astropy.constants as c

def redshift(z, wave, lum):
    lum = (lum * c.L_sun / u.Hz).to(u.erg / u.s / u.Hz).value
    if z == 0:
        return (wave, lum)
    else:
        Dl = Planck18.luminosity_distance(z)
        Dl.to(u.m)
        return ((1+z)*wave, lum/(4*np.pi*Dl.to(u.cm).value**2)/(1+z))
        #angstrom, 

def interp_filter(filt, spec_wavs, filter_wavs):
    return np.interp(spec_wavs, filter_wavs, filt)

def int_over_filter(flux, wavs, filt):
    
    filter_curve = interp_filter(filt.throughput, wavs, filt.wave)
    if filt.photon_counter:
        integrand = flux * filter_curve / wavs
        result = np.trapz(integrand, wavs)

        norm = np.trapz(filter_curve / wavs, wavs)
#        print('photon')

    else:
        integrand = flux * filter_curve
        result = np.trapz(integrand, x=wavs)

        norm = np.trapz(filter_curve, x=wavs)
#        print('energy')
    return result / norm

def generate_SED(filters, spec, wavelenghts):
    peaks = np.array([])
    Es = np.array([])
    for filt in filters:
        SED_point = int_over_filter(spec, wavelenghts, filt)
        peaks = np.append(peaks, filt.pivot)
        Es = np.append(Es, SED_point)
    return peaks, Es