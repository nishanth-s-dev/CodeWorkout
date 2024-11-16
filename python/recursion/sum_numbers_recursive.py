# https://www.structy.net/problems/sum-numbers-recursive
def sum_numbers_recursive(numbers):
  if not numbers:
    return 0
  return numbers[0] + sum_numbers_recursive(numbers[1:])