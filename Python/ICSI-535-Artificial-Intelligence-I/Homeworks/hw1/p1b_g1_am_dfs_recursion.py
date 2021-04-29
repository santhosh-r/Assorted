from hw1_common import g1_am, search_am

def __dfs(graph, start, goal, visited, path=[]):
  visited.append(start)
  path = path.copy() + [start]
  r = None
  for i, v in enumerate(graph[start]):
    if r is not None:
      break
    if v == 1:
      if i == goal:
        visited.append(i)
        r = path + [i]
      elif i not in visited:
        r = __dfs(graph, i, goal, visited, path)
  return r

def dfs(graph, start, goal, visited):
  return search_am(__dfs, graph, start, goal, visited)

def main():
  v = []
  r = dfs(g1_am, 'S', 'G', v)
  print('DFS-Recursion with undirected graph G1 (Adjacency Matrix)')
  print('Path returned:', r, '\nStates expanded:', v, end='')

if __name__ == '__main__':
  main()