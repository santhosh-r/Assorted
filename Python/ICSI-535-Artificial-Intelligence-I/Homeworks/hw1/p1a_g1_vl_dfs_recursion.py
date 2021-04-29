from hw1_common import g1_vl

def dfs(graph, start, goal, visited, path=[]):
  if start not in graph.keys():
    return None
  visited.append(start)
  path = path.copy() + [start]
  adjacent = graph[start]
  r = None
  for a in adjacent:
    if r is not None:
      break
    if a == goal:
      visited.append(a)
      return path + [a]
    elif a not in visited:
      r = dfs(graph, a, goal, visited, path)
  return r

def main():
  v = []
  r = dfs(g1_vl, 'S', 'G', v)
  print('DFS-Recursion with undirected graph G1 (Vertex List)')
  print('Path returned:', r, '\nStates expanded:', v, end='')

if __name__ == '__main__':
  main()