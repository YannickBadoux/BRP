import numpy as np
import fsps
from tqdm import tqdm
import os
import matplotlib.pyplot as plt
import scipy as sc


sp = fsps.StellarPopulation(compute_vega_mags=False, zcontinuous=1, sfh=0, logzsol=0.0, add_dust_emission=False,
    frac_nodust=1, frac_obrun=1)

# metaZ = np.linspace(0, 5, 10)
ages = np.linspace(0.01,13.7, )


fig, ax2 = plt.subplots(1,1)

        
 
for n in tqdm(ages):
    wave, spec = sp.get_spectrum(tage=n)
    ax2.plot(wave, spec, label=f"{n}")
    # ax2.set_xlim(0, 0.2e6)
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.legend()
plt.show()