from hw2_common import build_tree, print_tree
import math

def minimax(tree, height, alpha=-math.inf, beta=math.inf):
  tree.setVisited(True)
  if height == 0:
    return tree.getNodeValue()
  if tree.getOperationFlag() == 'max':
    v = max(-math.inf, minimax(tree.getLeftChild(), height - 1, alpha, beta))
    if v < beta:
      alpha = max(alpha, v)
      v = max(v, minimax(tree.getRightChild(), height - 1, alpha, beta))
      if v < beta: alpha = max(alpha, v)
  elif tree.getOperationFlag() == 'min':
    v = min(math.inf, minimax(tree.getLeftChild(), height - 1, alpha, beta))
    if v > alpha:
      beta = min(beta, v)
      v = min(v, minimax(tree.getRightChild(), height - 1, alpha, beta))
      if v > alpha: beta = min(beta, v)
  tree.setNodeValue(v)
  return v  


def main():
  tree = build_tree([3, 10, 2, 9, 10, 7, 5, 9, 2, 5, 6, 4, 2, 7, 9, 1], True, 4)
  print_tree(tree, 'minimax_pruning_input.png')
  chosen_terminal_state = minimax(tree, 4)
  print("The chosen terminal state:", chosen_terminal_state)
  print_tree(tree, 'minimax_pruning_output.png', True)
  
if __name__ == "__main__":
    main()