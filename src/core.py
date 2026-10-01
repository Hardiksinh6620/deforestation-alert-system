import numpy as np
from .validation import same_shape,finite
def normalized_difference(nir,red):
    nir=finite(nir,"nir"); red=finite(red,"red"); same_shape(nir,red); d=nir+red
    return np.divide(nir-red,d,out=np.full_like(nir,np.nan),where=d!=0)
def vegetation_loss(nir_before,red_before,nir_after,red_after,threshold=.15):
    before=normalized_difference(nir_before,red_before); after=normalized_difference(nir_after,red_after)
    return (before-after)>threshold
def change_magnitude(before,after):
    before=finite(before,"before"); after=finite(after,"after"); same_shape(before,after); return after-before
