from inspect import stack

from Node import get_default_tree, Node

# Preorder
def depth_first_values(root):
    if root is None:
        return []
    return [root.val] + depth_first_values(root.left) + depth_first_values(root.right)

# Inorder
def depth_first_values(root):
    if root is None:
        return []
    return  depth_first_values(root.left) + [root.val] + depth_first_values(root.right)

# Postorder
def depth_first_values(root):
    if root is None:
        return []
    return depth_first_values(root.left) + depth_first_values(root.right) + [root.val]

# Iterative
def depth_first_values(root):
    if root is None:
        return []
    stack = [ root ]
    res = []
    while stack:
        currentNode = stack.pop()
        if currentNode.left:
            stack.append(currentNode.left)
        if currentNode.right:
            stack.append(currentNode.right)
        res.append(currentNode.val)
    return res

root = get_default_tree()
print(depth_first_values(root))