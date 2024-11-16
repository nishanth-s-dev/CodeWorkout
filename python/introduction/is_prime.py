from math import sqrt

# https://www.structy.net/problems/is-prime
def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True
