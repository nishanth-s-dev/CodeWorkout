# https://www.structy.net/problems/intersection
def intersection(a, b):
  a_set = set(a)

  return [item for item in b if item in a_set]