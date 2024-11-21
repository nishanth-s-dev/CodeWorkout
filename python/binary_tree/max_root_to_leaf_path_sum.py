# https://www.structy.net/problems/max-root-to-leaf-path-sum

def max_path_sum(root):
    if root is None:
        return root
    stack = [(root, [root.val])]
    ans = float("-inf")
    while stack:
        current, path = stack.pop()
        if current.left is None and current.right is None:
            current_path_sum = sum(path)
            if current_path_sum > ans:
                ans = current_path_sum

        if current.left is not None:
            stack.append((current.left, path + [current.left.val]))
        if current.right is not None:
            stack.append((current.right, path + [current.right.val]))
    return ans

def max_path_sum(root):
    if root is None: return float("-inf")
    if root.left is None and root.right is None: return root.val
    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))