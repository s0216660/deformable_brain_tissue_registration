# Deformable tissue registrations

## Functionality

This python package allows to create brain tissue probability maps for grey matter (GM), wite matter (WM), and cerebrospinal fluid (CSF) for a specific patient. The method only takes a patient T1 image as an input and returns the tissue probability maps in patient space.

In case T1 isn't available, another modality image can be supplied. T1 should be preferred, because:

1. A T1 atlas image depicting normal adult brain anatomy (extracted from [sri24]) is used as a registration floating image,
2. pathologies such as brain tumors and lesions are less pronounced in T1, which is beneficial when performing registration with an atlas image depicting normal adult brain anatomy.

## Methods

The brain tissue probability maps are created via affine and non-rigid registration [2,3,4] from a healthy atlas [1] to patient space. [NiftiReg] is used for registration purposes. 

Registrations are calculated between a T1 image and the supplied patient T1 image, and the resulting transformations are then applied in parallel to the WM, GM and CSF atlas tissue probability maps:

An overview of the methodology can be described as follows:

1. An **affine registration** is calculated from atlas T1 to patient T1, resulting in 

 - an affine transformation matrix $T_{aff}$ (encoding the affine transformation) and,
 - a T1 atlas affinely registered to patient space, T1_aff_patient_space.
 
2. The resulting *affine transformation matrix* is applied to the WM, GM and CSF atlas tissue probability maps.

3. A **non-rigid (fast free-form deformable) registration** is calculated from the affinely registered T1 atlas to patient T1, resulting in 

 - a control point grid image (encoding the non-rigid transformation) and,
 
 - a T1 atlas deformably registered to patient space, T1_def_patient_space.
 
4. The resulting *control point grid image* is applied to the affinely registered WM, GM and CSF atlas tissue probability maps which were acquired in step 2. This leaves us with the deformably registered atlas tissue probability maps in patient space.

An illustrative overview is given below:

![alt text](https://bitbucket.org/s0216660/deformable-tissue-registrations/raw/466bd793faeae49419487c10d4b7c8f3d8a3c184/atlas_registration.pdf)

## Installation

This package makes use of NiftiReg, a library designed specifically for rigid, affine and non-rigid registrations. 

- [download available for Mac, Linux and Windows](https://sourceforge.net/projects/niftyreg/?source=navbar)
- [installation guidelines](https://cmiclab.cs.ucl.ac.uk/mmodat/niftyreg/wikis/install).

[sri24]: https://www.nitrc.org/projects/sri24/

[1]: T. Rohlfing, N. M. Zahr, E. V. Sullivan, and A. Pfefferbaum, “The SRI24 multichannel atlas of normal adult human brain structure,” Human Brain Mapping, vol. 31, no. 5, pp. 798-819, 2010. DOI: 10.1002/hbm.20906

[NiftiReg]: http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg

[2]: Modat, et al. (2014). Global image registration using a symmetric block-
matching approach. Journal of Medical Imaging, 1(2), 024003–024003.
doi:10.1117/1.JMI.1.2.024003

[3]: Rueckert, et al.. (1999). Nonrigid registration using free-form
deformations: Application to breast MR images. IEEE Transactions on Medical
Imaging, 18(8), 712–721. doi:10.1109/42.796284

[4]: Modat, et al. (2010). Fast free-form deformation using graphics processing
units. Computer Methods And Programs In Biomedicine,98(3), 278–284.
doi:10.1016/j.cmpb.2009.09.002