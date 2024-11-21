array = ["eat", "tea", "tan", "ate", "nat", "bat"]
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

def group_anagrams(array):
    hmap = {}
    for element in array:
        key = "".join(sorted(element))
        if key in hmap:
            hmap[key].append(element)
        if key not in hmap:
            hmap[key] = [element]
    return list(hmap.values())


print(group_anagrams(array))