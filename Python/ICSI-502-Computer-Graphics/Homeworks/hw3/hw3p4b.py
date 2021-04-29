#!/usr/bin/python3
"""
CSI 502 Homework 3 Problem 4b
Simple Hole Filling

@author: Santhosh

@comment
color_cube_w_holes.py modified so that holes don't share vertices
  otherwise unable to ascertain distinct holes and fill them.
Checked working for triangle.obj and bunny (with surface inverted
  to display properly in Open3D).
"""

import open3d
from mesh_io import HalfEdgeDS, IndexedFaceSet
from hw3p4a import is_watertight
from os import system

# Issue: will not work for holes with shared vertices
def find_holes(he_mesh):
  boundary_he = [he for he in he_mesh.halfedges if (he.face is None)]
  holes = []
  limit = len(boundary_he)
  while (len(boundary_he) > 0):
    hole = []
    he = boundary_he[0]
    for i in range(limit):
      hole.append(he)
      if (he.next == boundary_he[0]):
        holes.append(hole)
        break
      he = he.next
    for he in hole:
      boundary_he.remove(he)
  return holes

def fill_triangle_hole(he_mesh, hole):
  face = HalfEdgeDS.Face(hole[0])
  for he in hole:
    he.face = face
  he_mesh.faces.append(face)

def fill_holes(he_mesh, holes):
  for hole in holes:
    num = len(hole)
    if (num > 2):
      he1 = hole[0]
      v = hole[0].prev.vertex
      for i in range(1, num-2):
        he2 = HalfEdgeDS.HalfEdge(v=v, n=he1, p=hole[i])
        he1.next, he1.prev = hole[i], he2
        hole[i].next = he2
        fill_triangle_hole(he_mesh, [he1, hole[i], he2])
        he1 = HalfEdgeDS.HalfEdge(v=hole[i].vertex, t=he2)
        he2.twin = he1
        he_mesh.halfedges.append(he1)
        he_mesh.halfedges.append(he2)
      he1.next = hole[num-2]
      hole[num-1].next = he1
      fill_triangle_hole(he_mesh, [he1, hole[num-2], hole[num-1]])

def main():
  system('') # Enable VT100 Emulation for colors in Windows
  he_mesh = HalfEdgeDS(open3d.read_triangle_mesh('input/extra/color_cube_w_holes_mod.ply'))
  # he_mesh = HalfEdgeDS(IndexedFaceSet('input/extra/triangle.obj').get_mesh())
  # he_mesh = HalfEdgeDS(open3d.read_triangle_mesh('input/extra/bunny_meshlab.ply'))
  holes = find_holes(he_mesh)
  print('Finding holes...')
  print('Holes found:\x1B[32m', len(holes), '\x1B[0m')
  hole_sizes = [len(hole) for hole in holes]
  print('  Sizes of holes found:\x1B[32m', hole_sizes, '\x1B[0m')
  mesh = he_mesh.convert_to_IFS()
  mesh.compute_vertex_normals()
  open3d.draw_geometries([mesh])
  print('Filling holes...')
  fill_holes(he_mesh, holes)
  print('Holes yet to be filled:\x1B[32m', len(find_holes(he_mesh)), '\x1B[0m')
  print('Is filled mesh watertight?\x1B[32m', is_watertight(he_mesh), '\x1B[0m')
  mesh = he_mesh.convert_to_IFS()
  mesh.compute_vertex_normals()
  open3d.draw_geometries([mesh])
  
if __name__ == '__main__':
  main()