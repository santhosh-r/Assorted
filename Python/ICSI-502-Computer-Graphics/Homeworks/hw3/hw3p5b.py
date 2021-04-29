#!/usr/bin/python3
"""
CSI 502 Homework 3 Problem 5b
3D Mesh Simplification by Iterative Edge Collapsing 

@author: Santhosh

@comment
Not working
Fails for large number of simple edge deletions since faces
appear share an half-edge perhaps perhaps due to some
problem with my deletion algorithm
"""

import open3d
from mesh_io import HalfEdgeDS
from os import system
from hw3p4b import find_holes, fill_holes
from hw3p5a import delete_halfedge

def fill_mesh_holes(he_mesh):
  fill_holes(he_mesh, find_holes(he_mesh))

def main():
  system('') # Enable VT100 Emulation for colors in Windows
  # bunny modified to invert surface orientation of bunny.ply
  he_mesh = HalfEdgeDS(open3d.read_triangle_mesh('input/extra/bunny_meshlab.ply'))
  fill_mesh_holes(he_mesh)
  print('Displaying Original Mesh (after filling any holes)...')
  print('Vertices:\x1B[32m', len(he_mesh.vertices),
    '\x1B[0mEgdes:\x1B[32m', int(len(he_mesh.halfedges)/2),
    '\x1B[0mFaces:\x1B[32m', len(he_mesh.faces), '\x1B[0m')
  mesh = he_mesh.convert_to_IFS()
  mesh.compute_vertex_normals()
  mesh.paint_uniform_color([0.428, 0.428, 0.428])
  open3d.draw_geometries([mesh])
  for i in range(1000):
    delete_halfedge(he_mesh, he_mesh.halfedges[200])
  print('Displaying Mesh with first x edges deleted...')
  print('Vertices:\x1B[32m', len(he_mesh.vertices),
    '\x1B[0mEgdes:\x1B[32m', int(len(he_mesh.halfedges)/2),
    '\x1B[0mFaces:\x1B[32m', len(he_mesh.faces), '\x1B[0m')
  mesh = he_mesh.convert_to_IFS()
  mesh.compute_vertex_normals()
  open3d.draw_geometries([mesh])


if __name__ == '__main__':
  main()