# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def longest_streak(head):
    if head is None:
        return 0

    prev = head
    current = head.next

    current_res = 1
    res = float("-inf")

    while current is not None:
        if current.val == prev.val:
            current_res += 1
        else:
            res = max(res, current_res)
            current_res = 1
        prev = current
        current = current.next
    return max(current_res, res)