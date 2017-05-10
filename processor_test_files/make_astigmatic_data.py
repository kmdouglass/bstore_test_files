# © All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE,
# Switzerland, Laboratory of Experimental Biophysics, 2016-2017
# See the LICENSE.txt file for more details.

import numpy as np

# Create artificial calibration curves
z  = np.arange(-800, 800, 10)
wx = 0.0005 * (z - 150)**2 + 150
wy = 0.0005 * (z + 150)**2 + 150
              
# Create wobble curves
x = np.linspace(-25, 25, num=len(z))
y = np.linspace(-30, 30, num=len(z))

# Save output
np.savetxt(
    'calibration_curves.csv',
    np.transpose(
        (z, x, y, wx, wy)),
    delimiter=',',
    fmt='%.4f',
    header='z [nm],x [nm],y [nm],sigma_x [nm],sigma_y [nm]',
    comments='')
