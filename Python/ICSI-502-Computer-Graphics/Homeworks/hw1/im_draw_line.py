#!/usr/bin/python3
"""
CSI 502 Homework 1 Question 1

Example of drawing a line or rectangle to an image
Created on Fri Jan 07 10:50:24 2013

@author: mcchang

@comments
(Santhosh) Professor Chang's code for line and rectangle given in im_draw_line.py was modified to work without check_img_draw
"""

import numpy as np

def sort_xy(x1, y1, x2, y2):
  """Sort x and y values to used as indices."""
  if (x1 < x2):
    xmin, xmax = x1, x2
  else:
    xmin, xmax = x2, x1
  if (y1 < y2):
    ymin, ymax = y1, y2
  else:
    ymin, ymax = y2, y1
  return xmin, ymin, xmax, ymax

def img_draw_rect(img, x1, y1, x2, y2, v):
  """Draw a rectangle from (x1, y1) to (x2, y2) with the color v."""
  if (x1 == x2 and y1 == y2):
    img[y1, x1] = v
    return True
  xmin, ymin, xmax, ymax = sort_xy(x1, y1, x2, y2)
  img[ymin, xmin:xmax+1] = v
  img[ymax, xmin:xmax+1] = v
  img[ymin:ymax+1, xmin] = v
  img[ymin:ymax+1, xmax] = v
  return True  

def img_draw_rect_filled(img, x1, y1, x2, y2, v):
  """Draw a filled rectangle from (x1, y1) to (x2, y2) with the color v."""
  if (x1 == x2 and y1 == y2):
    img[y1, x1] = v
    return True
  xmin, ymin, xmax, ymax = sort_xy(x1, y1, x2, y2)
  img[ymin:ymax+1, xmin:xmax+1] = v
  return True  

def img_draw_line(img, x1, y1, x2, y2, v):
  """Draw a line segment from (x1, y1) to (x2, y2) with the color v."""
  if (x1 == x2 and y1 == y2):
    img[y1, x1] = v
    return True
  xmin, ymin, xmax, ymax = sort_xy(x1, y1, x2, y2)
  # Vetical line
  if (x1 == x2):
    img[ymin:ymax+1, x1] = v
    return True
  # Horizontal line
  if (y1 == y2):
    img[y1, xmin:xmax+1] = v
    return True
  # Arbitrary line
  dx = xmax-xmin+1
  dy = ymax-ymin+1
  steps = dx if dx > dy else dy
  for i in range(steps+1):
    x = x1 + (x2-x1)*i/steps
    y = y1 + (y2-y1)*i/steps
    # Draw a point to pixel (x,y)
    img[int(y),int(x)] = v # modified to avoid index error
  return True


def main():
  # Draw a rectangle on a numpy array
  A = np.zeros(shape=(8,7))
  img_draw_rect_filled (A, 0, 0, 5, 6, 9)
  img_draw_rect (A, 1, 2, 5, 6, 10)
  img_draw_line (A, 1, 0, 5, 7, 11)
  print (A)


if __name__ == '__main__':
    main()

