# https://www.structy.net/problems/premium/how-high

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def how_high(root):
  if root is None:
    return -1
  return max(how_high(root.left) + 1, how_high(root.right) + 1)
