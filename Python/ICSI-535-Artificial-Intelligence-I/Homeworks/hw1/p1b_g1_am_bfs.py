from hw1_common import g1_am, get_path, search_am
from queue import deque

def __bfs(graph, start, goal, visited):
  q = deque([start])
  visited.append(start)
  parents = {start: -1}
  while len(q) > 0:
    if goal in visited:
      break
    v = q.popleft()
    for i, val in enumerate(graph[v]):
      if val == 1 and i not in visited:
        q.append(i)
        visited.append(i)
        parents.update({i: v})
        if i == goal:
          break
  return get_path(parents, goal, start)

def bfs(graph, start, goal, visited):
  return search_am(__bfs, graph, start, goal, visited)

def main():
  v = []
  r = bfs(g1_am, 'S', 'G', v)
  print('BFS with undirected graph G1 (Adjacency Matrix)')
  print('Path returned:', r, '\nStates expanded:', v, end='')

if __name__ == '__main__':
  main()