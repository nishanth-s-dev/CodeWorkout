# https://www.structy.net/problems/premium/flip-tree

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def flip_tree(root):
  if root is None:
    return
  swap_nodes(root)
  flip_tree(root.left)
  flip_tree(root.right)
  return root

def swap_nodes(node):
  node.left, node.right = node.right, node.left