#!/usr/bin/python3
"""
CSI 502 Homework 3 Problem 2a
Simple Rotation

@author: Santhosh

@comment
Created image array with lengthened dimensions to store rotated image.
Mapped pixel in rotated image to original image by multiplying position with
  rotation matrix with no interpolation.
"""

import numpy as np
from skimage import io
import itertools
from matplotlib import pyplot as plt 

def rotate_image_simple(image, theta):
  theta *= -1 # since y values increase going from top to bottom
  rot_matrix = [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
  corners = np.array([np.matmul(rot_matrix, [((i&2)>>1)*image.shape[1], (i&1)*image.shape[0]]) for i in range(4)])
  min_x, min_y = min(corners[:,0]), min(corners[:,1])
  max_x, max_y = max(corners[:,0]), max(corners[:,1])
  shape = [int(max_y-min_y+0.5), int(max_x-min_x+0.5)] + list(image.shape[2:])
  rot_image = np.zeros(tuple(shape), 'uint8')
  for py, px in itertools.product(*map(range, image.shape[:2])):
    rot_p = np.matmul(rot_matrix, [px, py])
    y = min(int(rot_p[1]-min_y+0.5), shape[0]-1)
    x = min(int(rot_p[0]-min_x+0.5), shape[1]-1)
    rot_image[y, x] = image[py, px]
  return rot_image

def show_image(image, title):
  io.imshow(image)
  plt.title(title)
  io.show()

def main():
  lena_image = io.imread('input/lenag.png')
  rot_lena = rotate_image_simple(lena_image, 35*np.pi/180)
  io.imsave("output/hw3p2a_simple.png", rot_lena)
  show_image(rot_lena, 'Rotation with no Interpolation')
  
if __name__ == '__main__':
  main()