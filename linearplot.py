# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:51:33 2019

@author: Student
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = np.linspace(-15, 15, 10)
y = 2*x + 2
y2 = -0.5*x + 2 #Perpendicular Slope to 2x is -0.5

plt.plot(x, y, color = "green", label = "y = 2x + 2")
plt.plot(x, y2, color = "red", label = "y = -0.5x + 2")
axes = plt.gca()
axes.set_aspect(aspect = "equal")
axes.set_xlim([-15, 15])
plt.xlabel("x")
plt.ylabel("y")
plt.show()

x = np.linspace(-5, 5, 10)
y = x**2
plt.plot(x, y, color = "green", label = "y = x^2")
