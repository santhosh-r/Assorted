#!/usr/bin/python3
"""
CSI 502 Homework 1 Question 3a & 3b

@author: Santhosh

@comments
Intersection code from https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/ as suggested.
The above code was converted from C++ to Python before using it.
"""

import numpy as np
import matplotlib.pyplot as plt
import argparse

### Begin converted C++ code

def onSegment(p, q, r): 
  if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
    q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])): 
      return True 
  
  return False

# // To find orientation of ordered triplet (p, q, r). 
# // The function returns following values 
# // 0 --> p, q and r are colinear 
# // 1 --> Clockwise 
# // 2 --> Counterclockwise 
def orientation(p, q, r): 
  # // See https://www.geeksforgeeks.org/orientation-3-ordered-points/ 
  # // for details of below formula. 
  val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]) 

  if (val == 0):
    return 0  # // colinear 

  return 1 if val > 0 else 2 # // clock or counterclock wise

# // The main function that returns true if line segment 'p1q1' 
# // and 'p2q2' intersect. 
def doIntersect(p1, q1, p2, q2):
    # // Find the four orientations needed for general and 
    # // special cases 
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
  
    # // General case 
    if (o1 != o2 and o3 != o4):
        return True

    # // Special Cases 
    # // p1, q1 and p2 are colinear and p2 lies on segment p1q1 
    if (o1 == 0 and onSegment(p1, p2, q1)):
      return True 
  
    # // p1, q1 and q2 are colinear and q2 lies on segment p1q1 
    if (o2 == 0 and onSegment(p1, q2, q1)):
      return True
  
    # // p2, q2 and p1 are colinear and p1 lies on segment p2q2 
    if (o3 == 0 and onSegment(p2, p1, q2)):
      return True
  
    #  // p2, q2 and q1 are colinear and q1 lies on segment p2q2 
    if (o4 == 0 and onSegment(p2, q1, q2)):
      return True
  
    return False # // Doesn't fall in any of the above cases

### End converted C++ code

def check_if_inside(polygon, point):
  """Check if the given point is inside the given polygon."""
  n = 0 # to store the number of intersections
  # check if any of the edges intersect with the left horizontal ray from point
  q = polygon[polygon.shape[0] - 1]
  for p in polygon:
    if doIntersect(q, p, (0, point[1]), point):
      n += 1
    q = p
  return (n%2 > 0), n

def main():
  # parse the command line arguments for the polygon and the point to be checked
  parser = argparse.ArgumentParser(description='Checks if the given point is inside the given polygon.')
  parser.add_argument("x", help="x value of the input point", type=int, nargs='?', default=212)
  parser.add_argument("y", help="y value of the input point", type=int, nargs='?', default=121)
  parser.add_argument("file", help="file containing the vertices of the polygon", type=str, nargs='?', default='input/hw1q3_i.txt')
  args = parser.parse_args()
  polygon = np.loadtxt(args.file, 'int') # load the corners of the polygon
  assert polygon.shape[1] == 2
  point = (args.x, args.y)

  plt.fill(*zip(*polygon), alpha=0.4, edgecolor=(0, 0, 0, 1)) # fill the polygon (code from q6b)
  plt.plot(point[0], point[1], 'k.') # mark the point
  results = check_if_inside(polygon, point)
  # output the results to the plot
  plt.text(0, 0, 'Inside? {}'.format(results[0]))
  plt.text(0, 25, 'Number of Intersections: {}'.format(results[1]))
  plt.text(0, 50, 'Point: {}'.format(point))
  plt.savefig('hw1q3_o.png') # save the plot as an image
  plt.show() # show the plot


if __name__ == '__main__':
    main()