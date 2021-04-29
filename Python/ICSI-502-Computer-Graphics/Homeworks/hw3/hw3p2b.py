#!/usr/bin/python3
"""
CSI 502 Homework 3 Problem 2b
Rotation with Bilinear Interpolation

@author: Santhosh

@comment
Created image array with lengthened dimensions to store rotated image.
Mapped pixel in rotated image to original image by multiplying position with
  rotation matrix with bilinear interpolation.
Rotated back to original position and cropped with original dimensions
  before saving difference.
"""

import numpy as np
from skimage import io
import itertools
from matplotlib import pyplot as plt 

def sample_bilinear(image, x, y):
  x1, y1 = int(x), int(y)
  x2, y2 = min(x1+1, image.shape[1]-1), min(y1+1, image.shape[0]-1)
  # denominators ignored as x2 - x1 = y2 - y1 = 1, at the edges 0
  fxy1 = (x2 - x)*image[y1, x1] + (x - x1)*image[y1, x2]
  fxy2 = (x2 - x)*image[y2, x1] + (x - x1)*image[y2, x2]
  return (y2 - y)*fxy1 + (y - y1)*fxy2

def rotate_image_bilinear(image, theta):
  theta *= -1 # since y values increase going from top to bottom
  rot_matrix = [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
  corners = np.array([np.matmul(rot_matrix, [((i&2)>>1)*image.shape[1], (i&1)*image.shape[0]]) for i in range(4)])
  min_x, min_y = min(corners[:,0]), min(corners[:,1])
  max_x, max_y = max(corners[:,0]), max(corners[:,1])
  shape = [int(max_y-min_y+0.5), int(max_x-min_x+0.5)] + list(image.shape[2:])
  rot_image = np.zeros(tuple(shape), 'uint8')
  irot_matrix = [[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]]
  for py, px in itertools.product(*map(range, shape[:2])):
    irot_p = np.matmul(irot_matrix, [px+min_x, py+min_y])
    y = min(irot_p[1], shape[0]-1)
    x = min(irot_p[0], shape[1]-1)
    if (x>-1 and x<image.shape[1] and y>-1 and y<image.shape[0]):
      rot_image[py, px] = sample_bilinear(image, x, y)
  return rot_image

def crop_image_center(image, width, height=None):
  if (height is None):
    height = width
  shape = [height, width] + list(image.shape[2:])
  cropped_image = np.zeros(tuple(shape), 'uint8')
  sx, sy = int((image.shape[1]-shape[1])/2), int((image.shape[0]-shape[0])/2)
  for py, px in itertools.product(*map(range, shape[:2])):
    x, y = sx+px, sy+py
    if (x>-1 and x<image.shape[1] and y>-1 and y<image.shape[0]):
      cropped_image[py, px] = image[y, x]
  return cropped_image

def show_image(image, title):
  io.imshow(image)
  plt.title(title)
  io.show()

def main():
  lenag = io.imread('input/lenag.png')
  rot_lena = rotate_image_bilinear(lenag, 35*np.pi/180)
  io.imsave("output/hw3p2b_lenan.png", rot_lena)
  show_image(rot_lena, 'Rotation with Bilinear Interpolation')
  rot_lena = rotate_image_bilinear(rot_lena, -35*np.pi/180)
  lenag2 = crop_image_center(rot_lena, lenag.shape[1], lenag.shape[0])
  io.imsave("output/hw3p2b_lenag2.png", lenag2)
  diff = lenag - lenag2
  io.imsave("output/hw3p2b_diff.png", diff)
  show_image(diff, 'Difference after rotating back to original position')
  
if __name__ == '__main__':
  main()