#!/usr/bin/python3
"""
CSI 502 Homework 3 Problem 5a
Edge Collapse

@author: Santhosh

@comment
Collapsed edge by deleting one of its half-edge, reassigned
  neighboring half-edges twin and vertex values. For each
  half-edge, removed 6 halfedges, 2 faces and 1 vertex.
"""

import open3d
from mesh_io import HalfEdgeDS
from os import system
from random import randint

def get_face_halfedges(f):
  halfedges = []
  he = f.halfedge
  while (True):
    halfedges.append(he)
    he = he.next
    if (he == f.halfedge):
      break
  return halfedges

def delete_halfedge(he_mesh, he): 
  v1, v2 = he.vertex, he.prev.vertex
  h = he
  while (True):
    h.vertex = v2
    h = h.next.twin
    if (h == he):
      break
  for h in [he, he.twin]:
    h.next.twin.twin = h.prev.twin
    h.prev.twin.twin = h.next.twin
  he_mesh.vertices.remove(v1)
  for f in [he.face, he.twin.face]:
    for h in get_face_halfedges(f):
      he_mesh.halfedges.remove(h)
    he_mesh.faces.remove(f)

def main():
  system('') # Enable VT100 Emulation for colors in Windows
  # color_cube.py header modified so that Open3D can read the colors (eg. 'diffuse_red' -> 'r')
  mesh = open3d.read_triangle_mesh('input/extra/color_cube_mod.ply')
  he_mesh = HalfEdgeDS(mesh)
  print('Displaying Original Mesh...')
  print('Vertices:\x1B[32m', len(he_mesh.vertices),
    '\x1B[0mEgdes:\x1B[32m', int(len(he_mesh.halfedges)/2),
    '\x1B[0mFaces:\x1B[32m', len(he_mesh.faces), '\x1B[0m')
  mesh.compute_vertex_normals()
  open3d.draw_geometries([mesh])
  for i in range(5):
    print('Deleting random edge.')
    deletion_index = randint(0, len(he_mesh.halfedges)-1)
    delete_halfedge(he_mesh, he_mesh.halfedges[deletion_index])
    print('Displaying Mesh with {} random edge(s) deleted...'.format(i+1))
    print('Vertices:\x1B[32m', len(he_mesh.vertices),
      '\x1B[0mEgdes:\x1B[32m', int(len(he_mesh.halfedges)/2),
      '\x1B[0mFaces:\x1B[32m', len(he_mesh.faces), '\x1B[0m')
    mesh = he_mesh.convert_to_IFS()
    mesh.compute_vertex_normals()
    if (i == 0):
      open3d.write_triangle_mesh('output/hw3p5a.ply', mesh)
    open3d.draw_geometries([mesh])


if __name__ == '__main__':
  main()