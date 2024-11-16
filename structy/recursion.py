# https://www.structy.net/problems/sum-numbers-recursive
def sum_numbers_recursive(numbers):
  if not numbers:
    return 0
  return numbers[0] + sum_numbers_recursive(numbers[1:])

# https://www.structy.net/problems/premium/factorial
def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n - 1)

# https://www.structy.net/problems/premium/sum-of-lengths
def sum_of_lengths(strings):
  if not strings:
    return 0
  return len(strings[0]) + sum_of_lengths(strings[1:])

# https://www.structy.net/problems/premium/reverse-string-recursive
def reverse_string(s):
  if not s:
    return ''
  return reverse_string(s[1:]) + s[0]

# https://www.structy.net/problems/premium/palindrome-recursive
def palindrome(s):
  if not s:
    return True
  if s[0] != s[-1]:
    return False
  else:
    return palindrome(s[1:-1])

# https://www.structy.net/problems/premium/fibonacci
def fibonacci(n):
  if n == 0:
    return 0
  if n <= 2:
    return 1
  return fibonacci(n - 1) + fibonacci(n - 2)
