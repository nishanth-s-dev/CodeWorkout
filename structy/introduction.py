from math import sqrt


# https://www.structy.net/problems/hey-programmer
def greet(s):
  return "hey " + s

# https://www.structy.net/problems/max-value
def max_value(nums):
  res = float("-inf")
  for num in nums:
    if res < num:
      res = num
  return res

def max_value(nums):
    return max(nums)


# https://www.structy.net/problems/is-prime
def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True
