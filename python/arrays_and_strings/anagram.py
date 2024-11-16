from collections import Counter

# https://www.structy.net/problems/anagrams
def anagrams(s1, s2):
    return Counter(s1) == Counter(s2)