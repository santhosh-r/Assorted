from hw1_common import g2_am
from p1b_g1_am_dfs_recursion import dfs

def main():
  v = []
  r = dfs(g2_am, 'S', 'G', v)
  print('DFS-Recursion with directed graph G2 (Adjacency Matrix)')
  print('Path returned:', r, '\nStates expanded:', v, end='')

if __name__ == '__main__':
  main()