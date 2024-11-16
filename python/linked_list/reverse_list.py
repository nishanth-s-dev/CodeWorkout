# https://www.structy.net/problems/reverse-list
def reverse_list(head):
    stack = []
    current = head

    # Step 1: Push all nodes onto the stack
    while current is not None:
        stack.append(current)
        current = current.next

    # Step 2: Pop the last node as the new head
    head = stack.pop()
    current = head

    # Step 3: Reassign next pointers using the stack
    while stack:
        current.next = stack.pop()  # Link to the next node in reverse order
        current = current.next

    # Step 4: Set the last node's next pointer to None
    current.next = None

    return head

def reverse_list(head):
  current = head
  prev_node = None
  while current is not None:
    next_node = current.next
    current.next = prev_node
    prev_node = current
    current = next_node
  return prev_node

def reverse_list(head, prev=None):
    if head is None:
        return prev

    next_node = head.next
    head.next = prev
    return reverse_list(next_node, head)