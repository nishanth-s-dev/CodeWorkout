# https://www.structy.net/problems/premium/bottom-right-value

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


def bottom_right_value(root):
  if root is None:
    return None

  stack = [ (root, 0) ]
  max_level = -1
  res = None
  while stack:
    current, level = stack.pop()
    if current.left is not None:
      stack.append((current.left, level + 1))
    if current.right is not None:
      stack.append((current.right, level + 1))
    if current.right is None:
      if level > max_level:
        max_level = level
        res = current.val
  return res