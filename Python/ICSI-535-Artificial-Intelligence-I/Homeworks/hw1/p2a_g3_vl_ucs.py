from hw1_common import g3_vl, get_path
from queue import PriorityQueue

def ucs(graph, start, goal, visited):
  q = PriorityQueue()
  q.put((0, start))
  parents = {start: 0}
  cumulative_cost = {start: 0}
  while q:
    if goal in visited:
      break
    [vcost, v] = q.get()
    if v in visited:
      continue
    visited.append(v)
    if v == goal:
        break
    adjacent = [(c, graph[v][c]) for c in graph[v].keys() if c not in visited]
    for (c, ccost) in adjacent:
      ccost += vcost
      if c in cumulative_cost.keys() and ccost >= cumulative_cost[c]:
        continue
      q.put((ccost, c))
      parents.update({c: v})
      cumulative_cost.update({c: ccost})
  return get_path(parents, goal, start)

def main():
  v = []
  r = ucs(g3_vl, 'S', 'G', v)
  print('UCS with undirected graph G3 (Vertex List)')
  print('Path returned:', r, '\nStates expanded:', v, end='')

if __name__ == '__main__':
  main()