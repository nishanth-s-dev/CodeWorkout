# https://www.structy.net/problems/premium/paired-parentheses
def paired_parentheses(string):
  stack = []
  for c in string:
    if c == "(":
      stack.append(c)
    if c == ")":
      if not stack:
        return False
      stack.pop()
  return False if stack else True