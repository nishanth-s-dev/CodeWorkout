class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
  if not values:
    return None

  head = None
  res = None
  for value in values:
    new_node = Node(value)
    if head is None:
      head = new_node
      res = head
    head.next = new_node
    head = head.next

  return res