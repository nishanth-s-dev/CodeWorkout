# https://www.structy.net/problems/max-value
def max_value(nums):
  res = float("-inf")
  for num in nums:
    if res < num:
      res = num
  return res

def max_value(nums):
    return max(nums)