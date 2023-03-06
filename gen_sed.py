from eazy.filters import FilterFile
import numpy as np
import matplotlib.pyplot as plt
import fsps
import Function_file
from tqdm.notebook import tqdm


res = FilterFile(file='needed_curves', path='')
sp = fsps.StellarPopulation(compute_vega_mags=False, imf_type=0, zcontinuous=1, sfh=1, sf_trunc=.5, const=1, logzsol=0.0, add_dust_emission=False,
    frac_nodust=1, frac_obrun=1, agb_dust=0)

# ages = np.linspace(0.1, 9, 8)
# mets = [-1.84, 0, 0.46]

# fig, ax = plt.subplots(3,1, sharex=True, sharey=True, figsize=(10,20))
# for i in range(len(mets)):
#     sp.params["logzsol"] = mets[i]
#     for age in tqdm(ages):
#         wav, spec = sp.get_spectrum(tage=age)
#         peaks, Es = Function_file.generate_SED(res, spec, wav)

#         ax[i].scatter(peaks, Es, marker = ".", label = f"{round(age,2)} Gyr")
#         ax[i].set_ylabel('$f_{\\nu}  [L_{\odot}/Hz]$')
#         ax[i].set_title(f"logzsol = {mets[i]}")
# ax[0].legend()        
# ax[2].set_xlabel('wavelenght [$\AA$]')
# ax[0].set_xscale('log')
# ax[0].set_yscale('log')
# # ax.set_xlim(900, 20000)
# plt.show()

age = 5.
sp.params["logzsol"] = 0.
zred = [1, 2]

fig, ax = plt.subplots(2,1, figsize = (15,10), sharex= True, height_ratios=(2,1))
fig.subplots_adjust(hspace = 0)

wav, spec = sp.get_spectrum(tage = age)

for z in zred:
    twav, tspec = Function_file.redshift(z, wav, spec)
    peaks, Es = Function_file.generate_SED(res, tspec, twav)
    
    ax[0].plot(twav, tspec, label = f"z = {z}", zorder = 1, lw = 0.7)    
    ax[0].scatter(peaks, Es, label = f"z = {z} SED", zorder = 2, s = 28, edgecolor = "k")


for filt in res:
    ax[1].plot(filt.wave, filt.throughput, c = "k", lw = 0.4)

ax[0].legend()        
ax[1].set_xlabel('Wavelenght [$\AA$]')
ax[0].set_ylabel(r"$F_\nu\ [erg\ s^{-1}\ cm^{-2}\ Hz^{-1}]$")
ax[0].set_xscale('log')
ax[0].set_yscale('log')
ax[0].set_xlim(900, 120000)
# ax[0].set_ylim(1e-21, 2e-15)
ax[1].set_ylabel("Troughput")
# fig.suptitle(f"{age} Gyr old SSP spectra at different redshifts", fontsize = 16)

for ax in fig.get_axes():
    ax.label_outer()
plt.show()
