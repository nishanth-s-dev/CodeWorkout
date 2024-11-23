def tribonacci(n, memo={}):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    if n not in memo:
        memo[n] = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

    return memo[n]
