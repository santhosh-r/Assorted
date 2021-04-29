#!/usr/bin/python3
"""
CSI 502 Homework 2 Problem 4.3

IFS I/O Color

@author: Santhosh

@comment
"""
import open3d
import numpy as np
import mesh_io

def main():
  mesh = mesh_io.IndexedFaceSet("input/color_cube.ply").get_mesh()
  print(mesh)
  open3d.draw_geometries([mesh])
  
if __name__ == "__main__":
  main()