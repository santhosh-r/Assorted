from hw1_common import g4_am
from p2a_g3_am_ucs import ucs

def main():
  v = []
  r = ucs(g4_am, 'S', 'G', v)
  print('UCS with directed graph G4 (Adjacency Matrix)')
  print('Path returned:', r, '\nStates expanded:', v, end='')

if __name__ == '__main__':
  main()