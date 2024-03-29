# Deformable tissue registrations

## Functionality

This python package allows to create brain tissue probability maps for grey matter (GM), wite matter (WM), and cerebrospinal fluid (CSF) for a specific patient. The method only takes a patient T1 image as an input and returns the tissue probability maps in patient space.

In case T1 isn't available, another modality image can be supplied. T1 should be preferred, because:

1. A T1 atlas image depicting normal adult brain anatomy (extracted from [sri24]) is used as a registration floating image,
2. pathologies such as brain tumors and lesions are less pronounced in T1, which is beneficial when performing registration with an atlas image depicting normal adult brain anatomy.

## Methods

The brain tissue probability maps are created via affine and non-rigid registration [2,3,4] from a healthy atlas [1] to patient space. [NiftiReg] is used for registration purposes. 

Registrations are calculated between a T1 image and the supplied patient T1 image, and the resulting transformations are then applied in parallel to the WM, GM and CSF atlas tissue probability maps:

An illustrative overview is given below:

![alt text](https://bytebucket.org/s0216660/deformable-tissue-registrations/raw/210a739b50c4c30aaa9dc57cdceb77a28ad8b19b/atlas_registration.png?token=cfe6fe1423c6880bd7a7e7f0bae25ac77915a4a4)

The methodology can be described as follows:

1. Top row (left): An **affine registration** is calculated from atlas T1 to patient T1, resulting in:

    * an affine transformation matrix T_aff (encoding the affine transformation) and,
  
    * a T1 atlas affinely registered to patient space.
 
2. Middle row: The resulting **affine transformation matrix T_aff** is applied to the WM, GM and CSF atlas tissue probability maps.

3. Middle row (left): A **non-rigid (fast free-form deformable) registration** is calculated from the affinely registered T1 atlas to patient T1, resulting in: 

    * a control point grid image T_def (encoding the non-rigid transformation) and,
 
    * a T1 atlas deformably registered to patient space.
 
4. Bottom row: The resulting **control point grid image T_def** is applied to the affinely registered WM, GM and CSF atlas tissue probability maps (acquired in step 2). 

This results in the deformably registered atlas tissue probability maps in patient space.


## Installation

This package makes use of NiftiReg, a library designed specifically for rigid, affine and non-rigid registrations: 

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