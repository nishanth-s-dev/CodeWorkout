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

print(befitting_brackets('(){}[](())'))