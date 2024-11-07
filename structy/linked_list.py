class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

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

# https://www.structy.net/problems/linked-list-find
def linked_list_find(head, target):
  current = head
  while current is not None:
    if current.val == target:
      return True
    current = current.next
  return False

def linked_list_find(head, target):
  if head is None:
    return False
  if head.val == target:
    return True
  return linked_list_find(head.next, target)

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