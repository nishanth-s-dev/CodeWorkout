class Node:
    def __init__(self, val):
        self.val = val
        self.right, self.left = None, None

def get_default_tree():
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

    return a


#               a
#              / \
#             b   c
#            / \   \
#           d   e   f