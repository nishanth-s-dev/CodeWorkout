# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def is_univalue_list(head):
  if head is None:
    return head
  first = head.val
  current = head
  while current is not None:
    if current.val != first:
      return False
    current = current.next
  return True
