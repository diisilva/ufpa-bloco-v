"""A visual illustration of the various signal extension modes supported in
PyWavelets. For efficiency, in the C routines the array is not actually
extended as is done here. This is just a demo for easier visual explanation of
the behavior of the various boundary modes.

In practice, which signal extension mode is beneficial will depend on the
signal characteristics.  For this particular signal, some modes such as
"periodic",  "antisymmetric" and "zeros" result in large discontinuities that
would lead to large amplitude boundary coefficients in the detail coefficients
of a discrete wavelet transform.
"""
import numpy as np
from matplotlib import pyplot as plt
from pywt._doc_utils import boundary_mode_subplot
import pywt
from pywt import wavedec
import csv

path_csv = '/home/diego/Documentos/pds_sample_all/ufpa-bloco-v/pds_codes_imgs/sample_2.txt'
list_values = []

def listValues(path):
        
    with open(path, 'r') as f:
        # values_str = [line.strip() for line in f]
        for line in f:
            print line
            # break
            list_values.append(float(line))

    return list_values


def pywtCalculus2(listDistrib,typeDWT):
    
    coeffs = wavedec(listDistrib, typeDWT, level=2)

    cA2, cD2, cD1 = coeffs

    return cA2, cD2, cD1

def pywtCalculus(listDistrib,typeDWT):
    
    (ca, cd) = pywt.dwt(listDistrib,typeDWT)

    return ca,cd


def modesGraphs(listValues):
    
    # x = 5 - np.linspace(-1.9, 1.1, 9)**2

    # Create a figure with one subplots per boundary mode
    fig, axes = plt.subplots(3, 3, figsize=(10, 6))
    plt.subplots_adjust(hspace=0.5)
    axes = axes.ravel()
    boundary_mode_subplot(listValues, 'symmetric', axes[0], symw=False)
    boundary_mode_subplot(listValues, 'reflect', axes[1], symw=True)
    boundary_mode_subplot(listValues, 'periodic', axes[2], symw=False)
    boundary_mode_subplot(listValues, 'antisymmetric', axes[3], symw=False)
    boundary_mode_subplot(listValues, 'antireflect', axes[4], symw=True)
    boundary_mode_subplot(listValues, 'periodization', axes[5], symw=False)
    boundary_mode_subplot(listValues, 'smooth', axes[6], symw=False)
    boundary_mode_subplot(listValues, 'constant', axes[7], symw=False)
    boundary_mode_subplot(listValues, 'zeros', axes[8], symw=False)
    plt.show()

list_distrib = listValues(path_csv)

dwt = 'db1'
# c1,c2 = pywtCalculus(list_distrib,dwt)
ca1,cd2,cd1 = pywtCalculus2(list_distrib,dwt)
modesGraphs(cd2)



