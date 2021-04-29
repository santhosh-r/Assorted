from hw1_common import g1_am, search_am, get_path

def __dfs(graph, start, goal, visited):
  stack = [start]
  parents = {start: -1}
  while len(stack) > 0:
    v = stack.pop()
    visited.append(v)
    if v == goal:
      break
    col = graph[v]
    for i, val in enumerate(col):
      if val == 1 and i not in visited:
        stack.append(i)
        parents.update({i: v})
  return get_path(parents, goal, start)

def dfs(graph, start, goal, visited):
  return search_am(__dfs, graph, start, goal, visited)

def main():
  v = []
  r = dfs(g1_am, 'S', 'G', v)
  print('DFS-Stack with undirected graph G1 (Adjacency Matrix)')
  print('Path returned:', r, '\nStates expanded:', v, end='')

if __name__ == '__main__':
  main()
