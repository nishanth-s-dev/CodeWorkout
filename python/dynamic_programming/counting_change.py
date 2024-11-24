# https://www.structy.net/problems/counting-change

def counting_change(amount, coins):
    return _counting_change(amount, coins, 0, {})


def _counting_change(amount, coins, start_index, memo):
    if amount == 0:
        return 1
    if start_index == len(coins) or amount < 0:
        return 0

    key = (amount, start_index)
    coin = coins[start_index]

    if key not in memo:
        total_ways = 0
        for qty in range(0, (amount // coin) + 1):
            remainder = amount - (qty * coin)
            total_ways += _counting_change(remainder, coins, start_index + 1, memo)
        memo[key] = total_ways

    return memo[key]