class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_lists(head_1, head_2):
    res = Node(0)
    tail = res

    while head_1 is not None and head_2 is not None:
        if head_1.val <= head_2.val:
            tail.next = head_1
            head_1 = head_1.next
        else:
            tail.next = head_2
            head_2 = head_2.next
        tail = tail.next

    if head_1 is not None:
        tail.next = head_1
    if head_2 is not None:
        tail.next = head_2

    return res.next
