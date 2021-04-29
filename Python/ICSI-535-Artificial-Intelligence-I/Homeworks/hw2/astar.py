from hw2_common import graph_vl, graph_h, get_path
# from hw2_common import ex_vl as graph_vl, ex_h as graph_h, get_path
# from hw2_common import ex2_vl as graph_vl, ex2_h as graph_h, get_path
from queue import PriorityQueue

def astar(graph, h, start, goal, visited):
  q = PriorityQueue()
  q_ctr = 0 # used to ensure latest insertion has priority when f(n)=g(n)+h(n) is same
  q.put((0, q_ctr, start))
  q_ctr += 1
  parents = {start: 0}
  distance_from_start = {start: 0}
  while q:
    _, _, v = q.get()
    if v in visited:
      continue
    visited.append(v)
    if v == goal:
        break
    adjacent = [(c, graph[v][c]) for c in graph[v].keys() if c not in visited]
    for (c, ccost) in adjacent:
      ccost += distance_from_start[v]
      if c in distance_from_start.keys() and ccost >= distance_from_start[c]:
        continue
      parents.update({c: v})
      q.put((ccost + h[c], -q_ctr, c))
      q_ctr += 1
      distance_from_start.update({c: ccost})
  return get_path(parents, goal, start)

def main():
  v = []
  r = astar(graph_vl, graph_h, 'S', 'G', v)
  print('A* search with undirected graph (Vertex List)')
  print('Path returned:', r, '\nStates expanded:', v, end='')

if __name__ == '__main__':
  main()