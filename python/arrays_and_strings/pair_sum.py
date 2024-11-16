# https://www.structy.net/problems/pair-sum
def pair_sum(numbers, target_sum):
  counter = {}
  for index, num in enumerate(numbers):
    complement = target_sum - num
    if complement in counter:
      return (index, counter[complement])
    counter[num] = index