import numpy as np
from eazy.filters import FilterFile


def interp_filter(filter, spec_wavs, filter_wavs):
    return np.interp(spec_wavs, filter_wavs, filter)

def int_over_filter(flux, wavs, filt):
    
    filter_curve = interp_filter(filt.throughput, wavs, filt.wave)
    if filt.photon_counter:
        integrand = flux * filter_curve / wavs
        result = np.trapz(integrand, wavs)

        norm = np.trapz(filter_curve / wavs, wavs)
        print('photon')

    else:
        integrand = flux * filter_curve
        result = np.trapz(integrand, x=wavs)

        norm = np.trapz(filter_curve, x=wavs)
        print('energy')
    return result / norm

def generate_SED(filters, spec, wavelenghts):
    peaks = np.array([])
    Es = np.array([])
    for filt in filters:
        SED_point = int_over_filter(spec, wavelenghts, filt)
        peaks = np.append(peaks, filt.pivot)
        Es = np.append(Es, SED_point)
    return peaks, Es