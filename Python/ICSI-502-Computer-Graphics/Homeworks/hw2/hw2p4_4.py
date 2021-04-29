#!/usr/bin/python3
"""
CSI 502 Homework 2 Problem 4.4

Visualizing 3 ply mesh files from http://graphics.im.ntu.edu.tw/~robin/courses/gm05/model/ 

@author: Santhosh

@comment
Using MeshLab,
  horse.ply was converted from binary to ascii
  surface orientation of bunny.ply and horse.ply were inverted
"""
import open3d
import numpy as np
import mesh_io

def main():
  ply_meshes = ["input/bunny_meshlab.ply", "input/horse_meshlab.ply", "input/dragon.ply"]
  for i in range(3):
    mesh = mesh_io.IndexedFaceSet(ply_meshes[i]).get_mesh()
    # mesh = open3d.read_triangle_mesh(ply_meshes[i]) # same output as above
    print(ply_meshes[i], ":", mesh)
    mesh.compute_vertex_normals()
    mesh.paint_uniform_color([1, 0.706, 0])
    open3d.draw_geometries([mesh])
    
if __name__ == "__main__":
  main()