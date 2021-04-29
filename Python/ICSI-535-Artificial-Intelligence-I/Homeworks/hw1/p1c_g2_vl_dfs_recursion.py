from hw1_common import g2_vl
from p1a_g1_vl_dfs_recursion import dfs

def main():
  v = []
  r = dfs(g2_vl, 'S', 'G', v)
  print('DFS-Recursion with directed graph G2 (Vertex List)')
  print('Path returned:', r, '\nStates expanded:', v, end='')

if __name__ == '__main__':
  main()