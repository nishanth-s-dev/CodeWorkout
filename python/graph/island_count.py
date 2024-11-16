# https://www.structy.net/problems/island-count
def island_count(grid):
    visited = set()
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (row, col) not in visited:
                count += explore((row, col), grid, visited)
    return count


def explore(node, grid, visited):
    row, col = node
    if grid[row][col] == 'W':
        return 0
    stack = [node]
    while stack:
        current = stack.pop()
        visited.add(current)
        neighbors = get_neighbors(current, grid)
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
    return 1


def get_neighbors(node, grid):
    row, col = node
    up = (row - 1, col)
    right = (row, col + 1)
    down = (row + 1, col)
    left = (row, col - 1)

    res = []
    if row > 0 and grid[row - 1][col] == 'L':
        res.append(up)
    if col < len(grid[row]) - 1 and grid[row][col + 1] == 'L':
        res.append(right)
    if row < len(grid) - 1 and grid[row + 1][col] == 'L':
        res.append(down)
    if col > 0 and grid[row][col - 1] == 'L':
        res.append(left)
