#!/usr/bin/python3
"""
CSI 502 Homework 1 Question 6a

@author: Santhosh

@comments
Code from https://rosettacode.org/wiki/Voronoi_diagram as suggested.
Above code modified to load the given input "hand_pts.txt".
"""

from PIL import Image
import random
import math
import numpy as np
 
def generate_voronoi_diagram(nx, ny, width, height, num_cells):
  image = Image.new("RGB", (width, height))
  putpixel = image.putpixel
  imgx, imgy = image.size
  nr = []
  ng = []
  nb = []
  for i in range(num_cells):
    nr.append(random.randrange(256))
    ng.append(random.randrange(256))
    nb.append(random.randrange(256))
  for y in range(imgy):
    for x in range(imgx):
      dmin = math.hypot(imgx-1, imgy-1)
      j = -1
      for i in range(num_cells):
        d = math.hypot(nx[i]-x, ny[i]-y)
        if d < dmin:
          dmin = d
          j = i
      putpixel((x, y), (nr[j], ng[j], nb[j]))
   # (Santhosh) draw the input points on the output image
  for i in range(num_cells):
    for j in range(2):
      putpixel((nx[i]+j, ny[i]), (0, 0, 0))
      putpixel((nx[i]+j, ny[i]+1), (0, 0, 0))
  image.save('hw1q6a_o.png', 'PNG')
  image.show()
 
points = np.loadtxt('input/hand1_pts.txt') # (Santhosh) load points from the given input
width, height = 640, 480 # (Santhosh) set the output dimensions
 # (Santhosh) adjust input to match the output dimensions and convert to integers
xf = (width * 0.9)/np.max(points[:, 0])
yf = (height * 0.9)/np.max(points[:, 1])
nx = [int(x * xf) for x in points[:, 0]]
ny = [int(height - 24 - y*yf) for y in points[:, 1]]
generate_voronoi_diagram(nx, ny, width, height, len(nx))