class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def all_tree_paths(root):
  if root is None:
    return None

  stack = [(root, [root.val])]
  res = []
  while stack:
    current, path = stack.pop()
    if current.left is not None:
      stack.append((current.left, [current.left.val] + path))
    if current.right is not None:
      stack.append((current.right, [current.right.val] + path))

    if current.left is None and current.right is None:
      res.append(path)
  for path in res:
    path.reverse()
  return res

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

all_tree_paths(a) # ->
# [
#   [ 'a', 'b', 'd' ],
#   [ 'a', 'b', 'e' ],
#   [ 'a', 'c', 'f' ]
# ]