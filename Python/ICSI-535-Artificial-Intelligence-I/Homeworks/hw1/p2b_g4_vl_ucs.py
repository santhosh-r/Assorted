from hw1_common import g4_vl
from p2a_g3_vl_ucs import ucs

def main():
  v = []
  r = ucs(g4_vl, 'S', 'G', v)
  print('UCS with directed graph G4 (Vertex List)')
  print('Path returned:', r, '\nStates expanded:', v, end='')

if __name__ == '__main__':
  main()