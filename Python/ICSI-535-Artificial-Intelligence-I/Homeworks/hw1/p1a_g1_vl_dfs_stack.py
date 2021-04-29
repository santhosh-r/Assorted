from hw1_common import g1_vl, get_path

def dfs(graph, start, goal, visited):
  if start not in graph.keys() or goal not in graph.keys():
    return None
  stack = [start]
  parents = {start: 0}
  while len(stack) > 0:
    v = stack.pop()
    visited.append(v)
    if v == goal:
      break
    adjacent = list(graph[v])
    for a in adjacent:
      if a not in visited:
        stack.append(a)
        parents.update({a: v})
  return get_path(parents, goal, start)

def main():
  v = []
  r = dfs(g1_vl, 'S', 'G', v)
  print('DFS-Stack with undirected graph G1 (Vertex List)')
  print('Path returned:', r, '\nStates expanded:', v, end='')

if __name__ == '__main__':
  main()
