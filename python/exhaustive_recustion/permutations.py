def permutations(items):
    if not items:
        return [[]]
    first = items[0]
    permutations_without_first = permutations(items[1:])
    full_permutations = []
    for permutation in permutations_without_first:
        for i in range(len(permutation) + 1):
            full_permutations.append(permutation[:i] + [first] + permutation[i:])
    return full_permutations

print(permutations(['a', 'b', 'c']))