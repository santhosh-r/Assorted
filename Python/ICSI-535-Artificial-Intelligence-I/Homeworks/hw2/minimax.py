from hw2_common import build_tree, print_tree

def minimax(tree, height):
  path_left = path_right = []
  if height > 1:
    _, path_left = minimax(tree.getLeftChild(), height - 1)
    _, path_right = minimax(tree.getRightChild(), height - 1)
  left = tree.getLeftChild().getNodeValue()
  right = tree.getRightChild().getNodeValue()
  value = (min if tree.getOperationFlag() == 'min' else max)(left, right)
  tree.setNodeValue(value)
  return value, ['left'] + path_left if value == left else ['right'] + path_right


def main():
  tree = build_tree([3, 10, 2, 9, 10, 7, 5, 9, 2, 5, 6, 4, 2, 7, 9, 1], True, 4)
  print_tree(tree, 'minimax_input.png')
  chosen_terminal_state, output_path = minimax(tree, 4)
  print("The chosen terminal state:", chosen_terminal_state)
  print("The output path from root:", output_path)
  print_tree(tree, 'minimax_output.png')
  
if __name__ == "__main__":
    main()