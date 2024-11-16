from collections import Counter

# https://www.structy.net/problems/most-frequent-char
def most_frequent_char(s):
  frequency = Counter(s)
  return max(frequency, key=frequency.get)