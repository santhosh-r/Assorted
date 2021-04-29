#!/usr/bin/python3
"""
CSI 502 Homework 2

@author: Santhosh

@comment
Data Structure for Indexed Face Set
Simple read methods written with assumption there are no errors in obj and ply files.
"""

import numpy as np
import open3d

class IndexedFaceSet:
  def __init__(self, filename=None):
    self.vertices = []
    self.faces = []
    self.colors = []
    if filename is not None:
      self.read_file(filename)

  def read_file(self, filename):
    if (filename.split(".")[-1] == "obj"):
      self.read_file_obj(filename)
    elif (filename.split(".")[-1] == "ply"):
      self.read_file_ply(filename)
    else:
      print("mesh_io.py: Unknown format")

  def read_file_obj(self, filename):
    file = open(filename)
    for line in file:
      tokens = line.split()
      if (tokens[0] == 'v'):
        self.vertices.append([float(t) for t in tokens[1:]])
      elif (tokens[0] == 'f'):
        self.faces.append([int(t)-1 for t in tokens[1:]])
    
  def read_file_ply(self, filename):
    file = open(filename)
    header_done = False
    v_no = f_no = 0
    for line in file:
      tokens = line.split()
      if (tokens[0] == "element" and tokens[1] == "vertex"):
        v_no = int(tokens[2])
      elif (tokens[0] == "element" and tokens[1] == "face"):
        f_no = int(tokens[2])
      elif (tokens[0] == "end_header"):
        if (v_no == 0):
          break
        header_done = True
      elif (header_done == True):
        if(len(self.vertices) < v_no):
          self.vertices.append([float(t) for t in tokens[:3]])
          if (len(tokens) == 6):
            self.colors.append([int(t)/255.0 for t in tokens[3:6]])
        elif (len(self.faces) < f_no):
          self.faces.append([int(t) for t in tokens[1:]])

  def get_mesh(self):
    mesh = open3d.TriangleMesh()
    mesh.vertices = open3d.Vector3dVector(self.vertices)
    mesh.triangles = open3d.Vector3iVector(self.faces)
    mesh.vertex_colors = open3d.Vector3dVector(self.colors)
    return mesh

