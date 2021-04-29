#!/usr/bin/python3
"""
CSI 502 Homework 1 Question 2

@author: Santhosh

@comments
Code from Professor Chang's im_draw_line.py modifed and used.
Line function replaced with Bresenham's algorithm from readings. im_draw_line.py -> int_draw_line.py
Triangle fill code from http://www.sunshine2k.de/coding/java/TriangleRasterization/TriangleRasterization.html

No difference in output compared to Question 1.
"""

from skimage import io
import numpy as np
import time
from int_draw_line import img_draw_line, img_draw_rect, img_draw_rect_filled

TWO_PI = 2*np.pi

def img_draw_circle(img, x, y, r, v):
  """Draw a circle at (x, y) of radius r with the color v."""
  theta = 0
  dtheta = 1/(2*r)
  while (theta < TWO_PI):
    x1 = int(x + r*np.cos(theta))
    y1 = int(y + r*np.sin(theta))
    img[y1, x1] = v
    theta += dtheta
  return True

def img_draw_circle_filled(img, x, y, r, v):
  """Draw a filled circle at (x, y) of radius r with the color v."""
  range_r = range(r)
  r2 = r*r
  for i in range_r:
    i_2 = i*i
    for j in range_r:
      if (i_2 + j*j <= r2):
        img[y+j, x+i] = v
        img[y+j, x-i] = v
        img[y-j, x+i] = v
        img[y-j, x-i] = v
  return True

def img_draw_ellipse(img, x, y, a, b, v):
  """Draw an ellipse at (x, y) of axes a and b with the color v."""
  theta = 0
  dtheta = 1/(2*a)
  while (theta < TWO_PI):
    x1 = int(x + a*np.cos(theta))
    y1 = int(y + b*np.sin(theta))
    img[y1, x1] = v
    theta += dtheta
  return True

def img_draw_ellipse_filled(img, x, y, a, b, v):
  """Draw a filled ellipse at (x, y) of axes a and b with the color v."""
  range_b = range(b)
  for i in range(a):
    ia_2 = i*i/(a*a)
    for j in range_b:
      jb_2 = j*j/(b*b)
      if (ia_2 + jb_2 <= 1.0):
        img[y+j, x+i] = v
        img[y+j, x-i] = v
        img[y-j, x+i] = v
        img[y-j, x-i] = v
  return True

def img_draw_triangle(img, x1, y1, x2, y2, x3, y3, v):
  """Draw a triangle from the given points with the color v."""
  img_draw_line(img, x1, y1, x2, y2, v)
  img_draw_line(img, x2, y2, x3, y3, v)
  img_draw_line(img, x3, y3, x1, y1, v)
  return True

def sort_vertices_ascending_by_y(v1, v2, v3):
  """Sort the given vertices in ascending order of their y values."""
  l = [v1, v2, v3]
  l.sort(key=lambda s: s[1])
  return l[0], l[1], l[2]


### Begin converted Java code

def fillBottomFlatTriangle(img, v1, v2, v3, v):
  invslope1 = (v2[0] - v1[0]) / (v2[1] - v1[1])
  invslope2 = (v3[0] - v1[0]) / (v3[1] - v1[1])
  curx1 = v1[0]
  curx2 = v1[0]
  for scanlineY in range(v1[1], v2[1]+1):
    img_draw_line(img, int(curx1), scanlineY, int(curx2), scanlineY, v)
    curx1 += invslope1
    curx2 += invslope2

def fillTopFlatTriangle(img, v1, v2, v3, v):
  invslope1 = (v3[0] - v1[0]) / (v3[1] - v1[1])
  invslope2 = (v3[0] - v2[0]) / (v3[1] - v2[1])
  curx1 = v3[0]
  curx2 = v3[0]
  for scanlineY in reversed(range(v1[1]+1, v3[1]+1)):
    img_draw_line(img, int(curx1), scanlineY, int(curx2), scanlineY, v)
    curx1 -= invslope1
    curx2 -= invslope2

def img_draw_triangle_filled(img, v1, v2, v3, v):
  """Draw a filled triangle from the given points with the color v."""
  v1, v2, v3 = sort_vertices_ascending_by_y(v1, v2, v3)
  if (v2[1] == v3[1]):
    fillBottomFlatTriangle(img, v1, v2, v3, v)
  elif (v1[1] == v2[1]):
    fillTopFlatTriangle(img, v1, v2, v3, v)
  else:
    v4 = (int((v1[0] + float(v2[1] - v1[1]) / float(v3[1] - v1[1])) * (v3[0] - v1[0])), v2[1])
    fillBottomFlatTriangle(img, v1, v2, v4, v)
    fillTopFlatTriangle(img, v2, v4, v3, v)

### End converted Java code


A = np.zeros((480, 640), 'uint8')
img_draw_rect(A, 48, 115, 148, 215, 255)
img_draw_rect_filled(A, 48, 265, 148, 365, 255)
img_draw_circle(A, 246, 165, 50, 255)
img_draw_circle_filled(A, 246, 315, 50, 255)
img_draw_ellipse(A, 394, 165, 50, 25, 255)
img_draw_ellipse_filled(A, 394, 315, 50, 25, 255)
img_draw_triangle(A, 492, 215, 542, 115, 592, 215, 255)
img_draw_triangle_filled(A, (492, 365), (542, 265), (592, 365), 255)
io.imsave('hw1q2_o.png', A)
