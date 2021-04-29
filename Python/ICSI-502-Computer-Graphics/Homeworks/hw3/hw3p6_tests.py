# Testing neighbor function while debugging skew problem in hw3p6
# Skewed result was caused by my incorrect use of np.sum()

import numpy as np
import open3d
from mesh_io import HalfEdgeDS
from hw3p6 import find_neighboring_vertices
from random import randint
from sys import stdout

# manually comparing neighbors
def compare_neighbors_manually():
  mesh = open3d.read_triangle_mesh('input/extra/icosahedron.ply')
  for i in range(len(mesh.vertices)):
    neighbors = set()
    for tri in np.asarray(mesh.triangles):
      if i in tri:
        neighbors.update(tri)
    print(i, neighbors)
  print('')
  he_mesh = HalfEdgeDS(mesh)
  for vertex in he_mesh.vertices:
    neighbors = find_neighboring_vertices(vertex)
    nvi = []
    for n in neighbors:
      nvi.append(n.index)
    print(vertex.index, nvi)

# compare neighbors and return boolean result
def test_find_neighbors(mesh, he_mesh):
  ind = randint(0, len(he_mesh.vertex_data)-1)
  neighbors = find_neighboring_vertices(he_mesh.vertices[ind])
  center = he_mesh.vertices[ind].index
  nvi = [n.index for n in neighbors]
  for tri in np.asarray(mesh.triangles):
    if center in tri:
      # print(tri)
      for ind in tri:
        if ind not in [center]+nvi:
          return False
  # print(center, nvi)
  return True

def print_wo_nl(string):
  stdout.write(string)
  stdout.flush()

def main():
  # compare_neighbors_manually()
  # mesh = open3d.read_triangle_mesh('input/extra/color_cube_mod.ply')
  mesh = open3d.read_triangle_mesh('input/Armadillo.ply')
  print_wo_nl('Converting to Half-Edge Data Structure...')
  he_mesh = HalfEdgeDS(mesh)
  n = 10
  print_wo_nl('Done.\nTesting for {} vertices...'.format(n))
  result = True
  for _ in range(n):
    if (test_find_neighbors(mesh, he_mesh) == False):
      result = False
      break
  print('Done.\nAll neighbors found for', n, 'vertices?', result)    


if __name__ == '__main__':
  main()