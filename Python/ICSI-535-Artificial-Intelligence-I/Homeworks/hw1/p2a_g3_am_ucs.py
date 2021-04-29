from hw1_common import g3_am, get_path, search_am
from queue import PriorityQueue

def __ucs(graph, start, goal, visited):
  q = PriorityQueue()
  q.put((0, start))
  parents = {start: 0}
  cumulative_cost = {start: 0}
  while not q.empty():
    if goal in visited:
      break
    [vcost, v] = q.get()
    if v in visited:
      continue
    visited.append(v)
    if v == goal:
        break
    for i, ccost in enumerate(graph[v]):
      if ccost > 0 and i not in visited:
        ccost += vcost
        if i in cumulative_cost.keys() and ccost >= cumulative_cost[i]:
          continue
        q.put((ccost, i))
        parents.update({i: v})
        cumulative_cost.update({i: ccost})
  return get_path(parents, goal, start)

def ucs(graph, start, goal, visited):
  return search_am(__ucs, graph, start, goal, visited)

def main():
  v = []
  r = ucs(g3_am, 'S', 'G', v)
  print('UCS with undirected graph G3 (Adjacency Matrix)')
  print('Path returned:', r, '\nStates expanded:', v, end='')

if __name__ == '__main__':
  main()