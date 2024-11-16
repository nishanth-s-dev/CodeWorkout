# https://www.structy.net/problems/pair-product
def pair_product(numbers, target_product):
  counter = {}
  for index, num in enumerate(numbers):
    complement = target_product // num
    if complement in counter:
      return (index, counter[complement])
    counter[num] = index