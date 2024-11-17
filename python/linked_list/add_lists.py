class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def add_lists(head_1, head_2):
    dummy_head = Node(None)
    tail = dummy_head

    current_one = head_1
    current_two = head_2
    carry = 0
    while current_one is not None or current_two is not None or carry == 1:
        val_one = 0 if current_one is None else current_one.val
        val_two = 0 if current_two is None else current_two.val

        sum = val_one + val_two + carry
        carry = 1 if sum > 9 else 0

        digit = sum % 10
        tail.next = Node(digit)
        tail = tail.next

        if current_one is not None:
            current_one = current_one.next
        if current_two is not None:
            current_two = current_two.next

    return dummy_head.next

def add_lists(head_1, head_2, carry = 0):
  if head_1 is None and head_2 is None and carry == 0:
    return None

  val_one = 0 if head_1 is None else head_1.val
  val_two = 0 if head_2 is None else head_2.val

  sum = val_one + val_two + carry
  next_carry = 1 if sum > 9 else 0

  result = Node(sum % 10)

  next_1 = None if head_1 is None else head_1.next
  next_2 = None if head_2 is None else head_2.next

  result.next = add_lists(next_1, next_2, next_carry)
  return result