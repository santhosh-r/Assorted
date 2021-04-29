#!/usr/bin/python3
"""
CSI 502 Homework 2 Problem 4

@author: Santhosh

@comment
Problem 4 which was left incomplete from HW2
  but HW3 requires Half-Edge data structure.
Implemented Half-Edge data structure in mesh_io.py and 
  completed this to test my data structure.
"""

import open3d
import mesh_io
from os import system

def main():
  system('') # Enable VT100 Emulation for colors in Windows
  mesh = open3d.read_triangle_mesh('input/Armadillo.ply')
  print('IFS Mesh:\x1B[32m', mesh, '\x1B[0m')
  print('Converting to Half-Edge Data Structure...')
  he_mesh = mesh_io.HalfEdgeDS(mesh)
  print('Converted Mesh:\x1B[32m', he_mesh, '\x1B[0m')
  print('Reverting to IFS...')
  mesh = he_mesh.convert_to_IFS()
  mesh.compute_vertex_normals()
  mesh.paint_uniform_color([1, 0.706, 0])
  print('Reverted Mesh:\x1B[32m', mesh, '\x1B[0m')
  open3d.draw_geometries([mesh])

if __name__ == '__main__':
  main()