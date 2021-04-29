#!/usr/bin/python3
"""
CSI 502 Homework 3
Half-Edge Mesh Data Structure needed for problems 4 onwards

@author: Santhosh

@comment
2019-04-06
Added Half Edge Data Structure. Using Open3D to read .ply mesh files instead of my previous data structure.
At this point, Half Edge DS implemented using references instead of indices.

Data Structure for Indexed Face Set
Simple read methods written with assumption there are no errors in obj and ply files.
"""

import numpy as np
import open3d


class HalfEdgeDS:
  def __init__(self, mesh=None):
    self.vertex_data = []
    self.vertex_colors = []
    self.halfedges = []
    self.vertices = []
    self.faces = []
    if (mesh is not None):
      self.convert_from_IFS(mesh)
  
  class HalfEdge:
    def __init__(self, f=None, v=None, t=None, n=None, p=None):
      self.face = f
      self.vertex = v
      self.twin = t
      self.next = n
      self.prev = p
      
  class Vertex:
    def __init__(self, i=None, he=None):
      self.index = i
      self.halfedge = he

  class Face:
    def __init__(self, he=None):
      self.halfedge = he

  def convert_from_IFS(self, mesh):
    self.vertex_data = mesh.vertices
    if (mesh.has_vertex_colors()):
      self.vertex_colors = mesh.vertex_colors
    he_dict = {}
    vert_dict = {}
    for f in np.asarray(mesh.triangles):
      face = prev = None
      for i in range(3):
        he = self.HalfEdge(p=prev)
        self.halfedges.append(he)
        # Using get() so that twin is set to None if not present
        twin = he_dict.get((f[i], f[i-1]))
        if (twin is not None):
          he.twin = twin
          twin.twin = he
          del he_dict[f[i], f[i-1]]
        else:
          # # collisions found in mobius5k-surface.ply, multiple faces with same directed edge?
          # if (he_dict.get((f[i-1], f[i])) is not None):
          #   collisions += 1
          he_dict[f[i-1], f[i]] = he
        vertex = vert_dict.get(f[i])
        if (vertex is None):
          vertex = self.Vertex(f[i], he)
          self.vertices.append(vertex)
          vert_dict[f[i]] = vertex
        he.vertex = vertex
        if (face is None):
          face = self.Face(he)
          self.faces.append(face)
        he.face = face
        if (prev is not None):
          prev.next = he
        prev = he
      face.halfedge.prev = prev
      prev.next = face.halfedge
    bvp = [key[::-1] for key in he_dict.keys()]
    next_dict = {}
    prev_dict = {}
    for pair in bvp:
      twin = he_dict[pair[::-1]]
      he = self.HalfEdge(t=twin, v=twin.prev.vertex)
      self.halfedges.append(he)
      he_dict[pair] = he
      twin.twin = he
      for p in bvp:
        # last match gets assigned, good enough for single boundary and holes w/o shared vertices?
        if (p[0] == pair[1]):
          next_dict[pair] = p
        if (p[1] == pair[0]):
          prev_dict[pair] = p
    for pair in bvp:
      he = he_dict[pair]
      he.next = he_dict[next_dict[pair]]
      he.prev = he_dict[prev_dict[pair]]

  def __get_face_indices(self, f):
    face = []
    he = f.halfedge
    while (True):
      face.append(he.vertex.index)
      he = he.next
      if (he == f.halfedge):
        break
    return face

  def convert_to_IFS(self):
    mesh = open3d.TriangleMesh()
    mesh.vertices = self.vertex_data
    if (len(self.vertex_colors) != 0):
      mesh.vertex_colors = self.vertex_colors
    faces = [self.__get_face_indices(f) for f in self.faces]
    mesh.triangles = open3d.Vector3iVector(faces)
    return mesh
  
  def __ref_to_ind(self):
    pass

  def __ind_to_ref(self):
    pass

  def __str__(self):
    return '{} with {} vertices, {} edges and {} faces.'.format(type(self).__name__,
      len(self.vertices), int(len(self.halfedges)/2), len(self.faces))


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
