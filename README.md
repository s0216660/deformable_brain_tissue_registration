# Deformable tissue registrations

## Functionality

This python package allows to create brain tissue probability maps for grey matter -gm-, wite matter -wm- and cerebrospinal fluid -csf- for a specific patient. The method only takes a patient T1 image as an input and returns the tissue probability maps in patient space.

In case T1 isnt available for your patient, another modality image can be supplied. However, T1 is preferred because

1. a T1 atlas image (sri24, normal adult brain anatomy) is used as a registration floating image,
2. pathologies such as brain tumors and lesions are less pronounced in T1, which is beneficial when performing registration with an atlas image depicting normal adult brain anatomy.

## Installation

This package makes use of NiftiReg, a library designed specifically for rigid, affine and non-rigid registrations. It can be downloaded for Mac, Linux and Windows:
https://sourceforge.net/projects/niftyreg/?source=navbar
An installation guide is provided at:
https://cmiclab.cs.ucl.ac.uk/mmodat/niftyreg/wikis/install
