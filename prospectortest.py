import fsps
import dynesty
import sedpy
import h5py, astropy
import numpy as np
from prospect.models.templates import TemplateLibrary, describe
from prospect.models import SpecModel
from prospect.fitting import lnprobfn, fit_model
from prospect.sources import CSPSpecBasis

bands = 'ugriz'
filters = sedpy.observate.load_filters([f'sdss_{b}0' for b in bands])
print(filters)
# obs = 
# TemplateLibrary.show_contents()
model_params = TemplateLibrary['ssp']
model = SpecModel(model_params)
print(model)

# sps = CSPSpecBasis(zcontinuous=1)
