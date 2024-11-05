from collections import Counter



def anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

def pair_sum(numbers, target_sum):
  counter = {}
  for index, num in enumerate(numbers):
    if num in counter:
        return (index, counter[num])
    counter[target_sum - num] = index

print(pair_sum([1, 2, 3, 4, 5], 5))