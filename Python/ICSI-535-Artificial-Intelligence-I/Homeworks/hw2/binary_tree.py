class BinaryTree():

  # def __init__(self,rootid):
  def __init__(self, value, operation_flag=None):
    self.left = None
    self.right = None
    # self.rootid = rootid
    self.value = value
    self.operation_flag = operation_flag
    self.visited = False

  def getLeftChild(self):
    return self.left
  def getRightChild(self):
    return self.right
  def setNodeValue(self,value):
    self.value = value
  def getNodeValue(self):
    return self.value
  def getOperationFlag(self):
    return self.operation_flag
  def setVisited(self, visited):
    self.visited = visited
  def getVisited(self):
    return self.visited
  

  def insertRight(self,newNode, operation_flag=None):
    if self.right == None:
      self.right = BinaryTree(newNode, operation_flag)
    else:
      tree = BinaryTree(newNode, operation_flag)
      tree.right = self.right
      self.right = tree

  def insertLeft(self,newNode, operation_flag=None):
    if self.left == None:
      self.left = BinaryTree(newNode, operation_flag)
    else:
      tree = BinaryTree(newNode, operation_flag)
      tree.left = self.left
      self.left = tree


def printTree(tree):
  if tree != None:
    printTree(tree.getLeftChild())
    print(tree.getNodeValue())
    printTree(tree.getRightChild())

def testTree():
  myTree = BinaryTree("l_0")
  myTree.insertLeft("l_10")
  myTree.insertRight("l_11")
  l10 = myTree.getLeftChild()
  l10.insertLeft("l_20")
  l10.insertRight("l_21")
  l11 = myTree.getRightChild()
  l11.insertLeft("l_22")
  l11.insertRight("l_23")

  printTree(myTree)
