#!/usr/bin/python3
"""
CSI 502 Homework 3 Problem 1
Scaling with Bilinear Interpolation

@author: Santhosh

@comment
Added Nearest Neighbor for comparison. Simply map all pixel in scaled image to original image.
Bilinear ref: https://en.wikipedia.org/wiki/Bilinear_interpolation
"""

import numpy as np
from skimage import io
import itertools
from matplotlib import pyplot as plt

def scale_nearest_neighbor(image, factor):
  r_shape = [int(np.round(d * factor)) for d in image.shape[:2]] + list(image.shape[2:])
  r_image = np.zeros(tuple(r_shape), 'uint8')
  for py in range(r_shape[0]):
    map_y = min(int(py/factor + 0.5), image.shape[0] - 1)
    for px in range(r_shape[1]):
      map_x = min(int(px/factor + 0.5), image.shape[1] - 1)
      r_image[py, px] = image[map_y, map_x]
  return r_image

def scale_bilinear(image, factor):
  r_shape = [int(np.round(d * factor)) for d in image.shape[:2]] + list(image.shape[2:])
  r_image = np.zeros(tuple(r_shape), 'uint8')
  for py, px in itertools.product(*map(range, r_image.shape[:2])):
    x, y = px/factor, py/factor
    x1, y1 = int(x), int(y)
    x2, y2 = min(x1+1, image.shape[1]-1), min(y1+1, image.shape[0]-1)
    # denominators ignored as x2 - x1 = y2 - y1 = 1, at the edges 0
    fxy1 = (x2 - x)*image[y1, x1] + (x - x1)*image[y1, x2]
    fxy2 = (x2 - x)*image[y2, x1] + (x - x1)*image[y2, x2]
    r_image[py, px] = (y2 - y)*fxy1 + (y - y1)*fxy2
  return r_image

def show_image(image, title):
  io.imshow(image)
  plt.title(title)
  io.show()

def main():
  factor = 1.65
  lena_image = io.imread('input/lenag.png')
  r_image = scale_nearest_neighbor(lena_image, factor)
  io.imsave('output/hw3p1_lenags_nn.png', r_image)
  show_image(r_image, 'Nearest Neighbor Scaling at {}x'.format(factor))
  r_image = scale_bilinear(lena_image, factor)
  r_diff = lena_image - scale_bilinear(r_image, 1/factor)
  io.imsave('output/hw3p1_lenags.png', r_image)
  show_image(r_image, 'Bilinear Scaling at {}x'.format(factor))
  io.imsave('output/hw3p1_diff.png', r_diff)
  show_image(r_diff, 'Residue after scaling back to original resolution')
  
if __name__ == '__main__':
  main()