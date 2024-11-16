# https://www.structy.net/problems/premium/palindrome-recursive
def palindrome(s):
  if not s:
    return True
  if s[0] != s[-1]:
    return False
  else:
    return palindrome(s[1:-1])