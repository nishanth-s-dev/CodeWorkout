def howSum(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers)
        if remainderResult is not None:
            remainderResult.append(num)
            return remainderResult

    return None

def howSumMemo(targetSum, numbers, memo = None):
    if memo is None: memo = {}
    if targetSum == 0: return []
    if targetSum < 0: return None

    if targetSum in memo: return memo[targetSum]

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSumMemo(remainder, numbers, memo)
        if remainderResult is not None:
            memo[targetSum] = remainderResult + [num]
            return memo[targetSum]

    memo[targetSum] = None
    return None


if __name__ == '__main__':
    print(howSumMemo(7, [2, 3]))
    print(howSumMemo(7, [5, 3, 4, 7]))
    print(howSumMemo(7, [2, 4]))
    print(howSumMemo(8, [2, 3, 5]))
    print(howSumMemo(300, [7, 14]))
