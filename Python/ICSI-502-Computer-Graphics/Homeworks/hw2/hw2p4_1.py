#!/usr/bin/python3
"""
CSI 502 Homework 2 Problem 4.1

IFS I/O

@author: Santhosh

@comment
The triangle is not visible upon running but rotating the camera brings it into view.
"""
import open3d
import numpy as np
import mesh_io

def main():
  mesh = mesh_io.IndexedFaceSet("input/triangle.obj").get_mesh()
  print(mesh)
  open3d.draw_geometries([mesh])
  
if __name__ == "__main__":
  main()