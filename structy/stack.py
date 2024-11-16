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

# https://www.structy.net/problems/premium/befitting-brackets
def befitting_brackets(string):
  brackets = {"}" : "{", ")" : "(", "]" : "["}

  stack = []

  for c in string:
    if c not in brackets:
      stack.append(c)
    else:
      if not stack or stack.pop() != brackets[c]:
        return False

  return len(stack) == 0

# https://www.structy.net/problems/premium/decompress-braces
def decompress_braces(string):
  stack = []
  for c in string:
    if c == "{":
      continue
    if c == "}":
      temp = []
      while stack:
        current = stack.pop()
        if current.isdigit():
          stack.append("".join(temp[::-1]) * int(current))
          break
        else:
          temp.append(current)
    else:
      stack.append(c)
  return "".join(stack)


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


nesting_score("[]")