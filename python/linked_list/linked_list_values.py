# https://www.structy.net/problems/linked-list-values

def linked_list_values(head):
    if head is None:
        return []
    return [head.val] + linked_list_values(head.next)

def linked_list_values(head):
    res = []
    current = head
    while current is not None:
        res.append(current.val)
        current = current.next
    return res