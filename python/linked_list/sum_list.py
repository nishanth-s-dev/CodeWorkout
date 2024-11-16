# https://www.structy.net/problems/sum-list
def sum_list(head):
    res = 0
    current = head
    while current is not None:
        res += current.val
        current = current.next
    return res

def sum_list(head):
    if head is None:
        return 0
    return head.val + sum_list(head.next)