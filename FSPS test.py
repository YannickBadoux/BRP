import fsps

# Initialize a StellarPopulation object
sp = fsps.StellarPopulation(zcontinuous=1)

# Set the age range of interest
ages = [1e6, 1e7, 1e8] # in years

# Generate the spectra
spectra = sp.get_spectrum(tage=ages, peraa=True)

# Plot the spectra
import matplotlib.pyplot as plt
for i, age in enumerate(ages):
    plt.plot(spectra[0], spectra[1][:,i], label='{} years'.format(age))
plt.xlabel('Wavelength (Angstroms)')
plt.ylabel('Flux (Luminosity per unit wavelength)')
plt.legend()
plt.show()
