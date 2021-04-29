#!/usr/bin/python3
"""
CSI 502 Homework 1 Question 4

@author: Santhosh

@comments
Sprites and stencils from http://en.wikipedia.org/wiki/Mask_(computing) as given.
Referenced the given code for reading and saving images.
"""

import numpy as np
from skimage import data, io
from skimage.viewer import ImageViewer
import cv2
import os

def main():
  sprite_image = io.imread('input/hw1q4_i.png')
  sprites = [] # assume 0 - background, 1 - mask, 2 - foreground
  si = np.loadtxt('input/hw1q4_i.txt', 'uint16') # load the sprite indices as integers
  assert si.shape == (6, 2) # check the number of indices loaded
  for i in range(0, 6, 2):
    y1, y2, x1, x2 = si[i, 1], si[i+1, 1], si[i, 0], si[i+1, 0]
    # make sure the indices loaded are within the dimensions of the input image
    assert x1 < sprite_image.shape[1] and x2 < sprite_image.shape[1]
    assert y1 < sprite_image.shape[0] and y2 < sprite_image.shape[0]
    sprites.append(sprite_image[y1:y2, x1:x2]) # copy the portion specified by the indices
    if (i > 0):
      i1 = int(i/2)
      # check if the dimensions of the input sprites and stencil match
      assert sprites[i1].shape == sprites[i1-1].shape
  # create the output directory if needed
  if not os.path.exists('hw1q4_o'):
    os.mkdir('hw1q4_o')
  # initialize the output video with mp4 format, 20 fps and the same dimensions as the input sprites
  output_video = cv2.VideoWriter('hw1q4_o.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20.0, sprites[0].shape[1::-1])
  # loop to move the sprite right by 1 pixel every frame
  for dx in range(sprites[0].shape[1]):
    # initialize the output as an empty array
    image = np.zeros(sprites[0].shape, 'uint8')
    # loop through every pixel
    for y in range(image.shape[0]):
      for x in range(image.shape[1]):
        x1 = (x - dx) % image.shape[1] # subtract to move the sprite right
        # output = (background AND mask) OR foreground
        image[y, x] = (sprites[0][y, x] & sprites[1][y, x1]) ^ sprites[2][y, x1]
    io.imsave('hw1q4_o/a{:04d}.png'.format(dx), image) # save the frame as an image
    # convert to BGR to preserve color and write the frame to the output video
    output_video.write(cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
  output_video.release() # close the output video


if __name__ == '__main__':
    main()