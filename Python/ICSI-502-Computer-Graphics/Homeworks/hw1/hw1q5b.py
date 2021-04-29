#!/usr/bin/python3
"""
CSI 502 Homework 1 Question 5b

@author: Santhosh

@comments
Code from https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.Delaunay.html as suggested.
Lines added to load the given input "hand1_pts.txt" and to save the output.
"""

import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

points = np.loadtxt('input/hand1_pts.txt') # (Santhosh) load points from the given input
tri = Delaunay(points)
plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.plot(points[:,0], points[:,1], 'o')
plt.savefig('hw1q5b_o.png') # (Santhosh) save the output as an image
plt.show()
