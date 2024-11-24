# https://www.structy.net/problems/max-path-sum

def max_path_sum(grid):
    return _max_path_sum(grid, 0, 0, {})


def _max_path_sum(grid, row, col, memo):
    pos = (row, col)
    if pos in memo:
        return memo[pos]

    if row == len(grid) or col == len(grid[row]):
        return 0
    if row == len(grid) - 1 and col == len(grid[row]) - 1:
        return grid[row][col]

    down_sum = _max_path_sum(grid, row + 1, col, memo)
    right_sum = _max_path_sum(grid, row, col + 1, memo)

    memo[pos] = grid[row][col] + max(down_sum, right_sum)
    return memo[pos]
