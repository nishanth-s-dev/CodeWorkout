# https://www.structy.net/problems/premium/nesting-score
def nesting_score(string):
  stack = [0]
  for c in string:
    if c == "[":
      stack.append(0)
    else:
      top = stack.pop()
      if top == 0:
        stack[-1] += 1
      else:
        stack[-1] += 2 * top
  return stack.pop()