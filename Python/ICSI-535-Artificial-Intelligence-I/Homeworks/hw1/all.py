import p1a_g1_vl_bfs
import p1a_g1_vl_dfs_recursion
import p1a_g1_vl_dfs_stack
import p1b_g1_am_bfs
import p1b_g1_am_dfs_recursion
import p1b_g1_am_dfs_stack
import p2a_g3_vl_ucs
import p2a_g3_am_ucs
from hw1_common import g1_vl, g1_am, g2_vl, g2_am
from hw1_common import g3_vl, g3_am, g4_vl, g4_am

def run_search(search, graph, title):
  v = []
  r = search(graph, 'S', 'G', v)
  print(title)
  print('Path returned:', r, '\nStates expanded:', v, '\n\n', end='')

def main():
  run_search(p1a_g1_vl_dfs_recursion.dfs, g1_vl, 'DFS-Recursion with undirected graph G1 (Vertex List)')
  run_search(p1a_g1_vl_dfs_stack.dfs, g1_vl, 'DFS-Stack with undirected graph G1 (Vertex List)')
  run_search(p1a_g1_vl_bfs.bfs, g1_vl, 'BFS with undirected graph G1 (Vertex List)')
  run_search(p1b_g1_am_dfs_recursion.dfs, g1_am, 'DFS-Recursion with undirected graph G1 (Adjacency Matrix)')
  run_search(p1b_g1_am_dfs_stack.dfs, g1_am, 'DFS-Stack with undirected graph G1 (Adjacency Matrix)')
  run_search(p1b_g1_am_bfs.bfs, g1_am, 'BFS with undirected graph G1 (Adjacency Matrix)')
  run_search(p1a_g1_vl_dfs_recursion.dfs, g2_vl, 'DFS-Recursion with directed graph G2 (Vertex List)')
  run_search(p1a_g1_vl_dfs_stack.dfs, g2_vl, 'DFS-Stack with directed graph G2 (Vertex List)')
  run_search(p1a_g1_vl_bfs.bfs, g2_vl, 'BFS with directed graph G2 (Vertex List)')
  run_search(p1b_g1_am_dfs_recursion.dfs, g2_am, 'DFS-Recursion with directed graph G2 (Adjacency Matrix)')
  run_search(p1b_g1_am_dfs_stack.dfs, g2_am, 'DFS-Stack with directed graph G2 (Adjacency Matrix)')
  run_search(p1b_g1_am_bfs.bfs, g2_am, 'BFS with directed graph G2 (Adjacency Matrix)')
  run_search(p2a_g3_vl_ucs.ucs, g3_vl, 'UCS with undirected graph G3 (Vertex List)')
  run_search(p2a_g3_am_ucs.ucs, g3_am, 'UCS with undirected graph G3 (Adjacency Matrix)')
  run_search(p2a_g3_vl_ucs.ucs, g4_vl, 'UCS with directed graph G4 (Vertex List)')
  run_search(p2a_g3_am_ucs.ucs, g4_am, 'UCS with directed graph G4 (Adjacency Matrix)')

if __name__ == '__main__':
  main()