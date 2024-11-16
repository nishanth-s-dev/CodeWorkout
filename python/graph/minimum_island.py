# https://www.structy.net/problems/minimum-island
def minimum_island(grid):
    visited = set()
    minimum_length = float("inf")
    found_land = False

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (row, col) not in visited and grid[row][col] == 'L':
                found_land = True
                island_size = explore((row, col), grid, visited)
                minimum_length = min(minimum_length, island_size)

    return minimum_length if found_land else 0


def explore(node, grid, visited):
    row, col = node
    if grid[row][col] == 'W' or node in visited:
        return 0

    stack = [node]
    length = 0
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        length += 1
        neighbors = get_neighbors(current, grid)
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
    return length


def get_neighbors(node, grid):
    row, col = node
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 'L':
            neighbors.append((new_row, new_col))

    return neighbors
