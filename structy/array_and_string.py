from collections import Counter


# https://www.structy.net/problems/anagrams
def anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

# https://www.structy.net/problems/most-frequent-char
def most_frequent_char(s):
  frequency = Counter(s)
  return max(frequency, key=frequency.get)

# https://www.structy.net/problems/pair-sum
def pair_sum(numbers, target_sum):
  counter = {}
  for index, num in enumerate(numbers):
    complement = target_sum - num
    if complement in counter:
      return (index, counter[complement])
    counter[num] = index

# https://www.structy.net/problems/pair-product
def pair_product(numbers, target_product):
  counter = {}
  for index, num in enumerate(numbers):
    complement = target_product // num
    if complement in counter:
      return (index, counter[complement])
    counter[num] = index

# https://www.structy.net/problems/uncompress
def uncompress(s):
  numbers = "0123456789"
  result = []

  i, j = 0, 0
  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:
      num = int(s[i:j])
      result.append(num * s[j])
      j += 1
      i = j
  return "".join(result)

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

# https://www.structy.net/problems/intersection
def intersection(a, b):
  a_set = set(a)

  return [item for item in b if item in a_set]

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