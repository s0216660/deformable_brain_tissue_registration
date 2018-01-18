'''
Created on Jan 18, 2018

@author: Esther Alberts
'''
import os

import paths
import atlas_registration as ar

ar.niftireg_nonrigid_atlas_registration(paths.T1_EXAMPLE, 
                                        os.path.dirname(paths.T1_EXAMPLE), 
                                        masked=True)