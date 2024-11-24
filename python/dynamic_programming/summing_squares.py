# https://www.structy.net/problems/summing-squares

def summing_squares(n):
    return _summing_squares(n, {})


def _summing_squares(n, memo):
    if n == 0:
        return 0
    if n < 0:
        return float('inf')

    if n not in memo:
        inbound_perfect_squares = [i ** 2 for i in range(1, int(n ** 0.5) + 1) if i ** 2 <= n]

        min_path = float("inf")
        for square in inbound_perfect_squares:
            min_path = min(min_path, _summing_squares(n - square, memo) + 1)

        memo[n] = min_path if min_path != float("inf") else 0
    return memo[n]

def summing_squares(n):
    return _summing_squares(n, {})

def _summing_squares(n, memo):
    if n == 0:
        return 0
    if n < 0:
        return float("inf")
    if n not in memo:
        min_path = float('inf')
        for i in range(1, int(n ** 0.5) + 1):
            square = i ** 2
            min_path = min(min_path, _summing_squares(n - square, memo) + 1)
            memo[n] = min_path if min_path != float("inf") else 0
    return memo[n]