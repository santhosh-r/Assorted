#!/usr/bin/python3
"""
CSI 502 Homework 1 Question 5a

@author: Santhosh

@comments
Code from https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.ConvexHull.html as suggested.
Lines added to load the given input "hand1_pts.txt" and to save the output.
"""

import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

points = np.loadtxt('input/hand1_pts.txt') # (Santhosh) load points from the given input
hull = ConvexHull(points)
plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
  plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'ro')
plt.savefig('hw1q5a_o.png') # (Santhosh) save the output as an image
plt.show()