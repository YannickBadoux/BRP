from eazy.filters import FilterFile
import numpy as np
import matplotlib.pyplot as plt
import fsps
import Function_file
from tqdm.notebook import tqdm


res = FilterFile(file='needed_curves', path='')
sp = fsps.StellarPopulation(compute_vega_mags=False, imf_type=0, zcontinuous=1, sfh=1, sf_trunc=.5, const=1, logzsol=0.0, add_dust_emission=False,
    frac_nodust=1, frac_obrun=1, agb_dust=0)

ages = np.linspace(0.1, 13.7, 8)
mets = [-1.84, 0, 0.46]

fig, ax = plt.subplots(3,1, sharex=True, sharey=True, figsize=(10,20))
for i in range(len(mets)):
    sp.params["logzsol"] = mets[i]
    for age in tqdm(ages):
        wav, spec = sp.get_spectrum(tage=age)
        peaks, Es = Function_file.generate_SED(res, spec, wav)

        ax[i].scatter(peaks, Es, marker = ".", label = f"{round(age,2)} Gyr")
        ax[i].set_ylabel('$f_{\\nu}  [L_{\odot}/Hz]$')
        ax[i].set_title(f"logzsol = {mets[i]}")
ax[0].legend()        
ax[2].set_xlabel('wavelenght [$\AA$]')
ax[0].set_xscale('log')
ax[0].set_yscale('log')
# ax.set_xlim(900, 20000)
plt.show()