
# 
# me: Will Martin
# data: 3.12.2015
# license: BSD
# 

"""
Run this program to look ad the amazon-meta data interactively.
"""


# future
from __future__ import print_function, division

import pandas as pd


# Make the file names to read in 
FILEROOT = 'les0822nh15t13_aer008'
WL_strings = ['_w0.466', '_w0.632', '_w1.646']
WLS = [0.466, 0.632, 0.646]

FILES_REF = [FILEROOT + wl + '.ref' for wl in WL_strings] 
FILES_MODIS = [FILEROOT + wl + 'rad.modis' for wl in WL_strings] 


# Define some vaiabiels for this data set
X = 20.                         # km horizontal domain
Y = 20.                         # km horizontal domain




# Read the REF files 
def read_file_ref(fname, X=20., Y=20.):
    """
    Read a high resolution file ending in .ref.
    """
    # Check that the file ends in .ref
    if not (fname[-4:] == ".ref"):
        raise ValueError("Error reading file {}. Expected ending, '.ref'.".format(fname))




    #  



hres_frames = []
for wl, fname in zip(WLS, FILES_REF):
    
