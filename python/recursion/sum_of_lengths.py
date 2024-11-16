# https://www.structy.net/problems/premium/sum-of-lengths
def sum_of_lengths(strings):
  if not strings:
    return 0
  return len(strings[0]) + sum_of_lengths(strings[1:])