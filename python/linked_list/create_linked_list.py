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

def create_linked_list(values, i = 0):
  if i == len(values):
    return None
  head = Node(values[i])
  head.next = create_linked_list(values, i + 1)
  return head
