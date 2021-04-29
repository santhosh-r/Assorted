#!/usr/bin/python3
"""
CSI 502 Homework 3 Problem 4a
Watertightness

@author: Santhosh

@comment
Initial algorithm for Half-Edge construction
  had boundary edges with no twin.
Changed Half-Edge construction so that boundary edges
  had their own twin half-edges with face pointing to None.
  Note: Found odd number of half-edges for mobius5k-surface.ply
    due to collisions present in vertex pair dict in constructing
    half-edge mesh.
Now, check only if half-edge present with no face for watertightness.  
"""

import open3d
from mesh_io import HalfEdgeDS
from os import system

def is_watertight(he_mesh):
  for he in he_mesh.halfedges:
    if (he.face is None):
      return False
  # # Old algorithm when boundary half edges had no twins
  # for f in he_mesh.faces:
  #   he = f.halfedge
  #   while (True):
  #     if (he.twin is None):
  #       return False
  #     he = he.next
  #     if (he == f.halfedge):
  #       break
  return True

def main():
  system('') # Enable VT100 Emulation for colors in Windows
  ply_meshes = ['input/color_cube.ply', 'input/mobius5k-surface.ply', 'input/bunny.ply']
  for file in ply_meshes:
    he_mesh = HalfEdgeDS(open3d.read_triangle_mesh(file))
    print('Converted \'{}\' to'.format(file), he_mesh)
    print('Is mesh from file \'{}\' watertight? \x1B[32m{}\x1B[0m'.format(file, is_watertight(he_mesh)))


if __name__ == '__main__':
  main()