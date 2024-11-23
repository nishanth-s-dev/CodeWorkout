# https://www.structy.net/problems/premium/binary-search-tree-includes


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def binary_search_tree_includes(root, target):
    if root is None:
        return False

    if root.val == target:
        return True

    return binary_search_tree_includes(root.left if target < root.val else root.right, target)