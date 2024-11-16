# https://www.structy.net/problems/five-sort
def five_sort(nums):
  start = 0
  end = len(nums) - 1
  while start < end:
    while nums[end] == 5 and end > start:
      end -= 1
    while nums[start] != 5 and start < end:
      start += 1
    if nums[start] == 5:
      nums[start], nums[end] = nums[end], nums[start]
      end -= 1
  return nums