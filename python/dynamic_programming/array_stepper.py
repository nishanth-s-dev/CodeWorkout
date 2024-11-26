# https://www.structy.net/problems/array-stepper

def array_stepper(numbers):
    return _array_stepper(numbers, 0, {})


def _array_stepper(numbers, i, memo):
    if i in memo:
        return memo[i]
    if i >= len(numbers) - 1:
        return True
    if numbers[i] == 0:
        return False

    max_step = numbers[i]
    for step in range(1, max_step + 1):
        if _array_stepper(numbers, i + step, memo):
            memo[i] = True
            return True
    memo[i] = False
    return False


print(array_stepper([2, 4, 2, 0, 0, 1]))
