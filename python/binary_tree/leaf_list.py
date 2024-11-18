from collections import deque

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def leaf_list(root):
  res = []
  if root is None:
    return res
  queue = deque([root])
  while queue:
    current = queue.popleft()
    if current.left is None and current.right is None:
      res.append(current.val)
    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)

  return res

def leaf_list(root, res = []):
  if root is None:
    return res
  if root.left is None and root.right is None:
    res.append(root.val)
  leaf_list(root.left, res)
  leaf_list(root.right, res)
  return res
