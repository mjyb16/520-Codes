# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:41:04 2019

@author: Student
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = np.linspace(0, 10, 50)
y = np.exp(-x)

data_out = np.column_stack((x, y))

np.savetxt("output.dat", data_out)

x, y = np.loadtxt("output.dat", unpack = True)
plt.plot(x, y)
plt.show()