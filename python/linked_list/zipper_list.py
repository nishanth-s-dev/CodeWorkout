# https://www.structy.net/problems/zipper-lists
def zipper_lists(head_1, head_2):
    if head_1 is None or head_2 is None:
        return head_1 if head_1 else head_2

    head = head_1
    head_1 = head_1.next
    current = head

    while head_1 is not None and head_2 is not None:
        current.next = head_2
        current = current.next
        head_2 = head_2.next

        current.next = head_1
        current = current.next
        head_1 = head_1.next

    if head_1 is not None:
        current.next = head_1
    if head_2 is not None:
        current.next = head_2

    return head

def zipper_lists(head_1, head_2):
    if head_1 is None or head_2 is None:
        return head_1 if head_1 else head_2

    next_1 = head_1.next
    next_2 = head_2.next

    head_1.next = head_2
    head_2.next = zipper_lists(next_1, next_2)

    return head_1