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
