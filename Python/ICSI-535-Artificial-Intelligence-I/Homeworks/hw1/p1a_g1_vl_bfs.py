from hw1_common import g1_vl, get_path
from queue import deque

def bfs(graph, start, goal, visited):
  q = deque([start])
  visited.append(start)
  parents = {start: 0}
  while len(q) > 0:
    if goal in visited:
      break
    v = q.popleft()
    adjacent = [c for c in graph[v] if c not in visited]
    for c in adjacent:
      q.append(c)
      visited.append(c)
      parents.update({c: v})
      if c == goal:
        break
  return get_path(parents, goal, start)

def main():
  v = []
  r = bfs(g1_vl, 'S', 'G', v)
  print('BFS with undirected graph G1 (Vertex List)')
  print('Path returned:', r, '\nStates expanded:', v, end='')

if __name__ == '__main__':
  main()