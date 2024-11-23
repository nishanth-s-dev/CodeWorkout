def min_change(amount, coins):
    res = _min_change(amount, coins, {})
    return res if res != float("inf") else -1


def _min_change(amount, coins, memo):
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return float("inf")

    min_coins = float("inf")
    for coin in coins:
        min_coins = min(min_coins, 1 + _min_change(amount - coin, coins, memo))
    memo[amount] = min_coins
    return memo[amount]
