from hw1_common import g2_vl
from p1a_g1_vl_bfs import bfs

def main():
  v = []
  r = bfs(g2_vl, 'S', 'G', v)
  print('BFS with directed graph G2 (Vertex List)')
  print('Path returned:', r, '\nStates expanded:', v, end='')

if __name__ == '__main__':
  main()