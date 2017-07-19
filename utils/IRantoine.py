import numpy as np
from joblib import Parallel, delayed

def interferenceRemoval(Pj,IRsmooth,IRthreshold,IRslope):
    """reduces interferences between source spectrograms by enforcing sparsity along the source index"""
    J     = Pj.shape[-1]
    model = np.sum(Pj,axis=-1)
    if IRsmooth[0] is not None:
        model = smooth(model,IRsmooth[0])
    if IRsmooth[1] is not None:
        model = smooth(model.T,IRsmooth[1]).T

    for j in range(J):
        if np.any(IRsmooth):
            PjhatSmooth=Pj[...,j].copy()
            if IRsmooth[0] is not None:
                PjhatSmooth = smooth(PjhatSmooth,IRsmooth[0])
            if IRsmooth[1] is not None:
                PjhatSmooth = smooth(PjhatSmooth.T,IRsmooth[1]).T
        else:
            PjhatSmooth=Pj[...,j]
        W= np.minimum(1,(PjhatSmooth+1.0)/(model+1.0))
        if IRthreshold:
            W=logit(W,IRthreshold,IRslope)
        Pj[...,j] *= W
    return Pj


#defining global variables
JOBLIB_NCORES = 4
JOBLIB_TEMPFOLDER = None
JOBLIB_BACKEND    = None #'threading'

from scipy import signal

def smoothLine(data,kernel):
    """helper function parallelized by smooth"""
    return signal.fftconvolve(data,kernel, mode='same')

def smooth(s,lengthscale,parallel=True):
    """smoothes s vertically"""
    if len(s.shape) == 1:
        s=s[...,None]
    nChans = s.shape[1]
    lengthscale=2*round(float(lengthscale)/2)
    W = np.hamming(min(lengthscale,s.shape[0]))
    W/= np.sum(W)
    if s.shape[1]>1:
        if parallel:
            njobs=JOBLIB_NCORES
        else:
            njobs=1

        slidingMean = (Parallel(n_jobs=njobs,backend=JOBLIB_BACKEND,temp_folder=JOBLIB_TEMPFOLDER)
                        (delayed(smoothLine)(s[:,chan],W) for chan in range(nChans)))
        return np.array(slidingMean).T
    else:
        return smoothLine(s[:,0],W)[...,None]

def logit(W,threshold, slope):
    """performs a logit compression around threshold with given slope"""
    return 1./(1.0+np.exp(-slope*(W-threshold)))
