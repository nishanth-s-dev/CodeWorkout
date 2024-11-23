def sum_possible(amount, numbers, memo={}):
    if amount == 0:
        return True
    if amount < 0:
        return False

    if amount in memo:
        return memo[amount]

    for number in numbers:
        if sum_possible(amount - number, numbers, memo):
            memo[amount] = True
            return True

    memo[amount] = False
    return memo[amount]