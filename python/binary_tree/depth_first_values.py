from Node import get_default_tree, Node

def depth_first_values(root):
    if root is None:
        return []
    return [root.val] + depth_first_values(root.left) + depth_first_values(root.right)

root = get_default_tree()
print(depth_first_values(root))