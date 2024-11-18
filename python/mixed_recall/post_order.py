# https://www.structy.net/problems/premium/post-order

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def post_order(root, res = []):
  if root is None:
    return res
  post_order(root.left)
  post_order(root.right)
  res.append(root.val)
  return res