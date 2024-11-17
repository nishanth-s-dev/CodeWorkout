def subsets(elements):
    if not elements:
        return [[]]
    first = elements[0]
    subsets_without_first = subsets(elements[1:])
    subsets_with_first = []
    for subset in subsets_without_first:
        subsets_with_first.append([first] + subset)
    return subsets_with_first + subsets_without_first

print(subsets([1, 2, 3]))