#!/usr/bin/python3
"""
CSI 502 Homework 3 Problem 6
3D Mesh Gaussian Smoothing 

@author: Santhosh

@comment
Using smoothing algorithm from HW document and link given https://stackoverflow.com/questions/2323209/mesh-smoothing-with-gaussian.
The output ply file for "Armadillo.ply" was twice smoothened.
"""
import numpy as np
import open3d
from mesh_io import HalfEdgeDS
from sys import stdout

def find_distance(vertex_data, v1, v2):
  return np.linalg.norm(vertex_data[v1.index] - vertex_data[v2.index])

def find_neighboring_vertices(vertex):
  he = vertex.halfedge
  neighbors = []
  while (True):
    neighbors.append(he.twin.vertex)
    he = he.twin.prev
    if (he == vertex.halfedge):
      break
  return neighbors

def find_average_length(vertex_data, vertex, neighbors=None):
  nv = find_neighboring_vertices(vertex) if neighbors is None else neighbors 
  return sum([find_distance(vertex_data, vertex, n) for n in nv])/len(nv)

def smoothen_mesh(he_mesh):
  v_data = he_mesh.vertex_data
  sv_data = np.copy(v_data)
  for vertex in he_mesh.vertices:
    neighbors = find_neighboring_vertices(vertex)
    sigma = find_average_length(v_data, vertex, neighbors)
    sigma = 1 if sigma == 0.0 else sigma
    weights = []
    for n in neighbors:
      distance = find_distance(v_data, vertex, n)
      # Removed factor (1/sigma*np.sqrt(2*np.pi)) I added from book as it removed by normalization
      weights.append(np.exp(distance*distance/(-2*sigma*sigma)))
    weights /= sum(weights)
    wnv = [v_data[neighbors[i].index]*weights[i] for i in range(len(neighbors))]
    sum_wnv = [0.0, 0.0, 0.0]
    for v in wnv:
      for xn in range(3):
        sum_wnv[xn] += v[xn]
    ## Mistake: sv_data[vertex.index] += np.sum(wnv)
    sv_data[vertex.index] += sum_wnv
  he_mesh.vertex_data = open3d.Vector3dVector(sv_data)

def print_alt(string):
  stdout.write(string)
  stdout.flush()

def main():
  # mesh = open3d.read_triangle_mesh('input/extra/icosahedron.ply') # Every edge has the same length -> Output shape = Input shape
  mesh = open3d.read_triangle_mesh('input/extra/color_cube_mod.ply')
  # mesh = open3d.read_triangle_mesh('input/Armadillo.ply')
  mesh.paint_uniform_color([0.428, 0.428, 0.428])
  mesh.compute_vertex_normals()
  print('Displaying Original Mesh.')
  open3d.draw_geometries([mesh])
  print_alt('Converting to Half-Edge Data Structure...')
  he_mesh = HalfEdgeDS(mesh)
  print_alt('Done.\nSmoothing Mesh...')
  smoothen_mesh(he_mesh)
  print('Done.\nDisplaying Smoothened Mesh.')
  mesh = he_mesh.convert_to_IFS()
  mesh.compute_vertex_normals()
  open3d.draw_geometries([mesh])
  open3d.write_triangle_mesh('output/hw3p6.ply', mesh)


if __name__ == '__main__':
  main()