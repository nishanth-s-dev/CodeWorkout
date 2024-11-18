from collections import deque


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


def tree_levels(root):
    res = []
    if root is None:
        return res
    queue = deque([(root, 0)])
    while queue:
        current_node, level = queue.popleft()

        if len(res) > level:
            res[level].append(current_node.val)
        else:
            res.append([current_node.val])

        if current_node.left is not None:
            queue.append((current_node.left, level + 1))
        if current_node.right is not None:
            queue.append((current_node.right, level + 1))
    return res