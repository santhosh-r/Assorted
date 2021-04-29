#!/usr/bin/python3
"""
CSI 502 Homework 1 Question 2

Example of drawing a line or rectangle to an image
Created on Fri Jan 07 10:50:24 2013

@author: mcchang

@comments
(Santhosh) Line code from http://members.chello.at/~easyfilter/bresenham.html posted on Blackboard.
(Santhosh) Professor Chang's code for rectangle given in im_draw_line.py was modified to work without check_img_draw
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

def img_draw_line(img, x0, y0, x1, y1, v):
  """Draw a line segment from (x0, y0) to (x1, y1) with the color v."""
  dx =  np.abs(x1-x0)
  sx = 1 if x0<x1 else -1
  dy = -np.abs(y1-y0)
  sy = 1 if y0<y1 else -1
  err = dx+dy
  e2 = 0 # error value e_xy      
  while (True):  # loop
    img[y0, x0] = v
    if (x0==x1 and y0==y1):
      break
    e2 = 2*err
    if (e2 >= dy):
      err += dy
      x0 += sx  # e_xy+e_x > 0
    if (e2 <= dx):
      err += dx
      y0 += sy  # e_xy+e_y < 0
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

