# https://www.structy.net/problems/uncompress
def uncompress(s):
  numbers = "0123456789"
  result = []

  i, j = 0, 0
  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:
      num = int(s[i:j])
      result.append(num * s[j])
      j += 1
      i = j
  return "".join(result)
