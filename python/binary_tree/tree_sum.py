from collections import deque

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):
  if root is None:
    return 0
  sum = 0
  queue = deque([root])
  while queue:
    current = queue.popleft()
    sum += current.val
    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)
  return sum
