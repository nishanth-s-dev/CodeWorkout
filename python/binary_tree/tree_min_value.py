# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
  if root is None:
    return float('inf')
  leftSmall = tree_min_value(root.left)
  rightSmall = tree_min_value(root.right)
  return min(root.val, leftSmall, rightSmall)