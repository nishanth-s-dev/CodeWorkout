# https://www.structy.net/problems/get-node-value
def get_node_value(head, index):
  res = None
  current = head
  currentIndex = 0
  while current is not None:
    if currentIndex == index:
      res = current.val
      break
    currentIndex += 1
    current = current.next
  return res

def get_node_value(head, index, currentIndex = 0):
  if head is None:
    return None
  if currentIndex == index:
    return head.val
  return get_node_value(head.next, index, currentIndex + 1)