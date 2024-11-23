# https://www.structy.net/problems/premium/level-averages

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def level_averages(root):
    if root is None:
        return []
    levels = {}
    res = []
    stack = [(root, 0)]

    while stack:
        current_node, level = stack.pop()

        if level not in levels:
            levels[level] = [current_node.val]
        else:
            levels[level].append(current_node.val)

        if current_node.left is not None:
            stack.append((current_node.left, level + 1))
        if current_node.right is not None:
            stack.append((current_node.right, level + 1))

    for values in levels.values():
        if values:
            res.append(sum(values) / len(values))
    return res