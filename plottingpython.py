# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:36:43 2019

@author: Student
"""

import numpy as np
import matplotlib.pyplot as plt

g = -9.8
t = np.linspace(1, 10, 20)

print(t)
#t = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

y = 1000. + g*t**2/2
print y

plt.plot(t, y, "v", color = "green", markersize = 12, label = "Mock Data Points")
plt.xlabel("Time")
plt.ylabel("Height")
plt.legend()
plt.show()

err = 0.05*y
plt.errorbar(t, y, yerr = err, fmt='v', label = "Mock data points", color = "red", capsize = 10, markersize = 12)
t_theory = np.linspace(0., 11., 56)

y_theory = 1000. + g*t_theory**2/2
plt.plot(t_theory, y_theory, label = "Theory", ls = '--', color = "green")
plt.xlabel("Time")
plt.ylabel("Height")
plt.legend()
plt.show()
