#!/usr/bin/python3
"""
CSI 502 Homework 2 Problem 5.1

Display surface normals for cube and Stanford bunny.

@author: Santhosh

@comment
"""
import open3d
import numpy as np

def normalize(vector, size):
  mag = np.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
  return vector*size/mag

def display_surface_normals(filename, size):
  mesh = open3d.read_triangle_mesh(filename)
  mesh.paint_uniform_color([0, 0, 0.353])
  vertices = np.asarray(mesh.vertices)
  triangles = vertices[np.array(mesh.triangles)]
  # calculate normals
  normal_lines = []
  for tri in triangles:
    u = tri[1] - tri[0]
    v = tri[2] - tri[0]
    normal = normalize(np.cross(u, v), size)
    center = (tri[0] + tri[1] + tri[2]) / 3
    normal_lines.append(center)
    normal_lines.append(center+normal)
  lines = [[i, i+1] for i in range(0, len(normal_lines), 2)]
  colors = [[1, 0, 0] for i in range(len(lines))]
  line_set = open3d.LineSet()
  line_set.points = open3d.Vector3dVector(normal_lines)
  line_set.lines = open3d.Vector2iVector(lines)
  line_set.colors = open3d.Vector3dVector(colors)
  open3d.draw_geometries([mesh, line_set])

def main():
  display_surface_normals("input/cube.ply", 0.5)
  display_surface_normals("input/bunny_meshlab.ply", 0.0025)
  
if __name__ == "__main__":
  main()