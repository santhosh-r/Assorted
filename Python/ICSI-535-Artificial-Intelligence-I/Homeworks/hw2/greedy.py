from hw2_common import graph_vl, graph_h, get_path
# from hw2_common import ex_vl as graph_vl, ex_h as graph_h, get_path
from queue import PriorityQueue

def greedy(graph, h, start, goal, visited):
  v = start
  parents = {start: 0}
  while True:
    visited.append(v)
    if v == goal:
        break
    adjacent = [(h[c], c) for c in graph[v].keys() if c not in visited]
    if len(adjacent) == 0:
      return []
    q = PriorityQueue()
    for ccost, c in adjacent:
      q.put((ccost, c))
    _, c = q.get()
    parents.update({c: v})
    v = c
  return get_path(parents, goal, start)

def main():
  v = []
  r = greedy(graph_vl, graph_h, 'S', 'G', v)
  print('Greedy Search with undirected graph (Vertex List)')
  print('Path returned:', r, '\nStates expanded:', v, end='')

if __name__ == '__main__':
  main()