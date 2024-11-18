from collections import deque
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def breadth_first_values(root):
  if root is None:
    return []
  queue = deque([root])
  res = []
  while queue:
    currentNode = queue.popleft()
    if currentNode.left is not None:
      queue.append(currentNode.left)
    if currentNode.right is not None:
      queue.append(currentNode.right)
    res.append(currentNode.val)
  return res