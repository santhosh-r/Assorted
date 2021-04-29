from binary_tree import BinaryTree
import pydot
from uuid import uuid1

graph_vl = {
  'A': {'B': 2, 'C': 2},
  'B': {'A': 2, 'D': 1},
  'C': {'A': 2, 'D': 8, 'F': 3},
  'D': {'S': 3, 'B': 1, 'C': 8, 'E': 2},
  'E': {'S': 9, 'D': 2, 'H': 8, 'R': 2},
  'F': {'C': 3, 'G': 2, 'R': 2},
  'G': {'F': 2},
  'H': {'E': 8, 'P': 4, 'Q': 4},
  'P': {'S': 1, 'H': 4, 'Q': 15},
  'Q': {'H': 4, 'P': 15},
  'R': {'E': 2, 'F': 2},
  'S': {'D': 3, 'E': 9, 'P': 1}
}

graph_h = {'A': 5, 'B': 7, 'C': 4, 'D': 7, 'E': 5, 'F': 2, 'H': 11, 'P': 14, 'Q': 12, 'R': 3, 'G': 0, 'S': 0}

ex_vl = {
  'A': {'S': 2, 'C': 4},
  'B': {'S': 3, 'D': 4},
  'C': {'A': 4, 'D': 1, 'G': 2},
  'D': {'S': 5, 'B': 4, 'C': 1, 'G': 5},
  'G': {'C': 2, 'D': 5},
  'S': {'A': 2, 'B': 3, 'D': 5}
}

ex_h = {'A': 2, 'B': 5, 'C': 2, 'D': 1, 'G': 0, 'S': 0}

ex2_vl = {
  'A': {'S': 1.5, 'B': 2},
  'B': {'A': 2, 'C': 3},
  'C': {'B': 3, 'G': 4},
  'D': {'S': 2, 'E': 3},
  'E': {'D': 3, 'G': 2},
  'G': {'C': 4, 'E': 2},
  'S': {'A': 1.5, 'D': 2}
}

ex2_h = {'A': 4, 'B': 2, 'C': 4, 'D': 4.5, 'E': 2, 'G': 0, 'S': 0}

def get_path(parents, end, start):
  if start not in parents.keys() or end not in parents.keys():
    return None
  path = [end]
  while path[0] != start:
    path = [parents[path[0]]] + path
  return path

def build_tree(terminal_values, is_maximizing, height, tree=None):
  if height < 1:
    return None
  operation_flag = 'max' if is_maximizing else 'min'
  if tree is None:
    tree = BinaryTree('', operation_flag)
    build_tree(terminal_values[::-1], not is_maximizing, height, tree)
    return tree
  if height == 1:
    tree.insertLeft(terminal_values.pop())
    tree.insertRight(terminal_values.pop())
  else:
    tree.insertLeft('', operation_flag)
    tree.insertRight('', operation_flag)
    build_tree(terminal_values, not is_maximizing, height - 1, tree.getLeftChild())
    build_tree(terminal_values, not is_maximizing, height - 1, tree.getRightChild())

def print_tree(tree, filename, is_output=False, graph=None, parent_node=None, parent_label=''):
  if tree is None:
    return
  graph = graph if graph else pydot.Dot(graph_type='digraph')
  shape = 'rectangle'
  value = tree.getNodeValue()
  if tree.getOperationFlag() == 'max':
    shape =  'triangle'
  elif tree.getOperationFlag() == 'min':
    shape =  'invtriangle'
  elif is_output:
    value = value if tree.getVisited() else ''
  node = pydot.Node(str(uuid1()), label=value, shape=shape)
  graph.add_node(node)
  if parent_node:
    graph.add_edge(pydot.Edge(parent_node, node))
  print_tree(tree.getLeftChild(), '', is_output, graph, node, value)
  print_tree(tree.getRightChild(), '', is_output, graph, node, value) 
  if parent_node is None:
    graph.write_png(filename)
