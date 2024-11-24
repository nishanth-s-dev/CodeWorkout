# https://www.structy.net/problems/count-paths

def count_paths(grid):
  return _count_paths(grid, 0, 0, {})

def _count_paths(grid, row, col, memo = {}):
  pos = (row, col)
  if pos in memo:
    return memo[pos]
  if row == len(grid) or col == len(grid[0]) or grid[row][col] == "X":
    return 0
  if row == len(grid) -1 and col == len(grid[0]) - 1:
    return 1
  memo[pos] = _count_paths(grid, row + 1, col) + _count_paths(grid, row, col + 1)
  return memo[pos]