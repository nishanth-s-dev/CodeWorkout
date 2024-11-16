# https://www.structy.net/problems/compress
def compress(s):
  res = []
  s += "!"

  i, j = 0, 0
  while j < len(s):
    if s[j] == s[i]:
      j += 1
    else:
      append_string(i, j, res, s)
      i = j
  # append_string(i, j, res, s)
  return "".join(res)

def append_string(i, j, res, s):
  current_string = s[i:j]
  if len(current_string) != 1:
    res.append(f"{len(current_string)}{s[i]}")
  else:
    res.append(s[i])