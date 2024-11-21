# https://www.structy.net/problems/premium/tree-path-finder

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def path_finder(root, target):
    if root is None: return None

    stack = [(root, [root.val])]
    while stack:
        current, path = stack.pop()

        if current.val == target:
            return path

        if current.left is not None:
            stack.append((current.left, path + [current.left.val]))
        if current.right is not None:
            stack.append((current.right, path + [current.right.val]))

    return None


def path_finder(root, target):
    if root is None:
        return None
    if root.val == target:
        return [root.val]
    left_path = path_finder(root.left, target)
    if left_path is not None:
        return [root.val, *left_path]
    right_path = path_finder(root.right, target)
    if right_path is not None:
        return [root.val, *right_path]
    return None